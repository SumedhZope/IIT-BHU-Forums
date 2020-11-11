$(document).ready(function(){
    resposive();
});
$(window).resize(function(){
    resposive();
});

function resposive(){
    var h = $(window).height()-$('.base_navbar').height()-$('.front').height();
    h /= 2;
    $('.front').css({'padding-top':h+'px'});
}


$(document).on('submit','#register-form-id', function(e){
    e.preventDefault();
    var btn_val = $(this).context.getElementsByClassName('btn')[0].value;
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
        success:function(data){
            if(data.result == 'success'){
                window.location.href = 'feed/';
            }else{
                $('#register_error').css({'display':'block'});
                $('#register_error').html(data.message);
            }
        },
        error:function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});

$(document).on('submit','#login-form-id', function(e){
    e.preventDefault();
    var btn_val = $(this).context.getElementsByClassName('btn')[0].value;
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
        success:function(data){
            if(data.result == 'success'){
                window.location.href = 'feed/';
            }else{
                $('#login_error').css({'display':'block'});
            }
        },
        error:function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});