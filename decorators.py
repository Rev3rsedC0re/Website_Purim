from flask import Flask, session, flash, redirect, url_for
from functools import wraps

def logged_in(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not "user" in session:
            if(not '_flashes' in session):
                flash("Not logged in",'danger')
            return redirect(url_for('login'))
        return func(*args,**kwargs)
    return wrapper

