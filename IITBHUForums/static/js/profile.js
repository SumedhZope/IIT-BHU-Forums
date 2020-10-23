
$(document).on('submit','#AddFriend', function(e){
    e.preventDefault();
    url = window.location.href+'/add_friend'
  //  console.log(url)
    $.ajax({
        type : 'POST',
        url : url,
        data : {
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            if(data.result == 'success'){
                $('#AddFriend').css({'display':'none'})
                $('#Friends_0').css({'display':'none'})
                $('#Friends').css({'display':'block'})
                $('#Friends').html('friend request sent')
                
            }else{
                alert(1);
            }
        },
        error:function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});

$(document).on('submit','#AcceptFriend', function(e){
    e.preventDefault();
    url = window.location.href+'/accept_friend'
  //  console.log(url)
    $.ajax({
        type : 'POST',
        url : url,
        data : {
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            if(data.result == 'success'){
                $('#AcceptFriend').css({'display':'none'})
                $('#Friends_0').css({'display':'none'})
                $('#DeclineFriend').css({'display':'none'})
                $('#Friends').css({'display':'block'})
                $('#Friends').html('you both are friends')
            }else{
                alert(1);
            }
        },
        error:function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});

$(document).on('submit','#DeclineFriend', function(e){
    e.preventDefault();
    url = window.location.href+'/decline_friend'
  //  console.log(url)
    $.ajax({
        type : 'POST',
        url : url,
        data : {
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            if(data.result == 'success'){
                $('#AcceptFriend').css({'display':'none'})
                $('#Friends_0').css({'display':'none'})
                $('#DeclineFriend').css({'display':'none'})
                $('#Friends').css({'display':'block'})
                $('#Friends').html('friend request declined')
            }else{
                alert(1);
            }
        },
        error:function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});