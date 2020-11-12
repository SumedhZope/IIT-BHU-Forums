$(document).ready(function(){
    resposive();
    preset();
    setting();
});

function resposive(){
    var h = $(window).height()-$('.base_navbar').height();
    h-=55;
    $('.container').css({'height':h+'px'});
}

const btn = document.getElementsByClassName('btn') 

Array.from(btn).forEach(element => {
    const id_main = element.id
    const inputElement = document.getElementById(id_main + '-input')
    const formData = document.getElementById(id_main + '-form')
    var loc = window.location
    var wsStart = 'ws://'
    var chatHolder = $('#'+id_main+'-chat-holder')
    var me = $('#myUsername').val()
    if (loc.protocol == 'https://'){
        wsStart = 'wss://'
    }

    var endpoint = wsStart + loc.host + '/chat/' + id_main + '/'
    var socket= new ReconnectingWebSocket(endpoint)

    socket.onmessage = function(e){
        var chatDataMsg = JSON.parse(e.data)
            if(chatDataMsg.message != ''){
                chatHolder.append("<li>" + chatDataMsg.message + " via - " + chatDataMsg.username +  "</li>")
            }
    }

    socket.onopen = function(e){
        element.addEventListener('click', function(event){
            event.preventDefault()
            var msgText = inputElement.value
            if(inputElement.value != ''){
                var finalData = {
                    'message' : msgText
                }
                socket.send(JSON.stringify(finalData))
            }
            inputElement.value = ''
        })
    }

    socket.onerror = function(e){
        console.log("error")
    }

    socket.onclose = function(e){
        console.log("close")
    }

});

function switch_chat(p){
    var s = p.id.slice(0,-5) + "-chats";
    $('.chats').css({'display':'none'});
    $('#'+s).css({'display':'block'});
    $('.all-names').css({'background-color':'#393E46'});
    $('#'+p.id).css({'background-color':'#222831'});
    $('#'+p.id).css({'':''});
    $('#'+p.id).css({'':''});
}

function preset(){
    pre = document.getElementById('preset');
    if(pre != null){
        document.getElementById(pre.classList[1] + "-name").click();
    }
}

function setting(){
    chat_boxes = document.getElementsByClassName('chat-holder');
    Array.from(chat_boxes).forEach(e =>{
        e.scrollTop = e.scrollHeight;
    });
}