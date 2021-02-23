document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + '/private');

    // When connected, configure buttons
    socket.on('connect', () => {
        document.querySelector('#editor').innerHTML = "Connected";
        socket.emit('join room',{"room_id":room_id});
    });
    
   
  

    // When a new vote is announced, add to the unordered list
    socket.on('send text', data => {
        document.querySelector('#editor').innerHTML = data;
    });
});