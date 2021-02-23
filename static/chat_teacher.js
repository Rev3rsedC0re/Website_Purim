document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + '/private');
    // When connected, configure buttons
    socket.on('connect', function() {
        socket.emit('create room', {'course':course});
        document.querySelector('#editor').onkeyup = function() {
                const text = this.value;
                socket.emit('change text', {'text': text});
        };
    });

    socket.on('room created', data => {
        document.querySelector('#meeting_id').innerHTML = data.id;
		document.querySelector('#meeting_pwd').innerHTML = data.pwd;
    });
});
