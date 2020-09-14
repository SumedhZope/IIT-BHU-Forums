$(document).ready(function(){
    resposive();
});
$(window).resize(function(){
    resposive();
});

function resposive(){
    var h = $(window).height()-$('.header').height()-$('.front').height();
    h /= 2;
    $('.front').css({'padding-top':h+'px'});
}


$(document).on('submit','#register-form-id', function(e){
    e.preventDefault();
    $.ajax({
        type : 'POST',
        url : '/',
        data : {
            username : $('#username').val(),
            email : $('#email').val(),
            password1 : $('#password1').val(),
            password2 : $('#password2').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            window.location.href = "testnav/"
        }
    });
});