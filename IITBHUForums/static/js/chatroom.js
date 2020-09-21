console.log('loaded')

const btn = document.getElementsByClassName('btn') 

Array.from(btn).forEach(element => {
    const id_main = element.id
    const inputElement = document.getElementById(id_main + '-input')
    const formData = document.getElementById(id_main + '-form')
    var loc = window.location
    console.log(loc)
    var wsStart = 'ws://'
    var chatHolder = $('#chat-items')
    var me = $('#myUsername').val()

    if (loc.protocol == 'https://'){
        wsStart = 'wss://'
    }

    var endpoint = wsStart + loc.host + '/chat/' + id_main + '/'
    var socket= new ReconnectingWebSocket(endpoint)

    socket.onmessage = function(e){
        console.log('msg')
        var chatDataMsg = JSON.parse(e.data)
            if(chatDataMsg.message != ''){
                chatHolder.append("<li>" + chatDataMsg.message + " via - " + chatDataMsg.username +  "</li>")
            }
    }

    socket.onopen = function(e){
        console.log('open')
        element.addEventListener('click', function(event){
            event.preventDefault()
            var msgText = inputElement.value
            if(inputElement.value != ''){
                var finalData = {
                    'message' : msgText
                }
                socket.send(JSON.stringify(finalData))
            }
        })
    }

    socket.onerror = function(e){
        console.log("error")
    }

    socket.onclose = function(e){
        console.log("close")
    }

});