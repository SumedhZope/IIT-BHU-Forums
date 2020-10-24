var loc = window.location
var formData = $('#form')
var msgInput = $('#id_message')
var wsStart = 'ws://'
var chatHolder = $('#chat-items')
var me = $('#myUsername').val()

if (loc.protocol == 'https://'){
    wsStart = 'wss://'
}

console.log(loc)

var endpoint = wsStart + loc.host + loc.pathname
var socket= new ReconnectingWebSocket(endpoint)

socket.onmessage = function(e){
    var chatDataMsg = JSON.parse(e.data)
    if(chatDataMsg.message != ''){
        chatHolder.append("<li>" + chatDataMsg.message + " via - " + chatDataMsg.username +  "</li>")
    }
}

socket.onopen = function(e){
    console.log('open')
    formData.submit(function(event){
        event.preventDefault()
        var msgText = msgInput.val()
        var finalData = {
            'message' : msgText
        }
        socket.send(JSON.stringify(finalData))
        msgInput.val('')
    })
}

socket.onerror = function(e){
    console.log("error")
}

socket.onclose = function(e){
    console.log("close")
}
