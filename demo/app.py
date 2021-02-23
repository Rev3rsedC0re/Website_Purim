from flask import Flask, render_template, jsonify, request, flash, redirect, url_for, session
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://dctrbzumwxwvxy:d9f3c10d641a04f27617fc2b950f0319119e8c461e4eaadca60d4567be4b6a00@ec2-54-210-128-153.compute-1.amazonaws.com:5432/d5tda9sutqok51"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'u083hh+3fevjs9-dfjv98u32uc98u98ufcu4usuf8ur88apidj98rmnrijfdj'
socketio = SocketIO(app)

@app.route("/")
def registration():
    return render_template("page.html")

@socketio.on("connect", namespace='/private')
def connect():
    print("client wants to connect")
    emit("status", { "data": "Connected. Hello!" })

@socketio.on("join",namespace='/private')
def on_join(data):
    user = data["user"]
    room = data["room"]
    print(f"client {user} wants to join: {room}")
    join_room(room)
    emit("room_message", f"Welcome to {room}, {user}", room=room)
    
if (__name__ == "__main__"):
    #Flask.run(app)
    #Flask.run(app,ssl_context='adhoc')
    socketio.run(app)
