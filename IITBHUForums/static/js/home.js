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
    var btn_val = $(this).context.getElementsByClassName('btn')[0].value;
    console.log(btn_val)
    $.ajax({
        btn : btn_val,
        type : 'POST',
        url : '/',
        data : {
            btn : btn_val,
            username_signup : $('#username-signup').val(),
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

$(document).on('submit','#login-form-id', function(e){
    e.preventDefault();
    var btn_val = $(this).context.getElementsByClassName('btn')[0].value;
    console.log(btn_val)
    $.ajax({
        btn : btn_val,
        type : 'POST',
        url : '/',
        data : {
            btn : btn_val,
            username_signin : $('#username-signin').val(),
            password : $('#password').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            window.location.href = 'testnav/'
        }
    });
});