$(document).on('submit','.AcceptFriend', function(e){
    e.preventDefault();
    id = $(this).context.getElementsByClassName('btn')[0].value
    url = '/profile/'+id+'/accept_friend'
  //  console.log(url)
    $.ajax({
        type : 'POST',
        url : url,
        data : {
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            if(data.result == 'success'){
                $('#'+id).css({'display':'none'})
            }else{
                alert(1);
            }
        },
        error:function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});

$(document).on('submit','.DeclineFriend', function(e){
    e.preventDefault();
    id = $(this).context.getElementsByClassName('btn')[0].value
    url = '/profile/'+id+'/decline_friend'
  //  console.log(url)
    $.ajax({
        type : 'POST',
        url : url,
        data : {
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            if(data.result == 'success'){
                $('#'+id).css({'display':'none'})
            }else{
                alert(1);
            }
        },
        error:function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});