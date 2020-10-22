
$(document).on('submit','#AddFriend', function(e){
    e.preventDefault();
    $.ajax({
        type : 'POST',
        url : window.location.href,
        data : {
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            if(data.result == 'success'){
                $('#AddFriend').css({'display':'none'})
                $('#Friends').css({'display':'block'})
            }else{
                
            }
        },
        error:function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});