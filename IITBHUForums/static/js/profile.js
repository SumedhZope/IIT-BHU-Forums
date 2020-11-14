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

const openTab_2 = (e, id_name) => {
    tabContent = document.getElementsByClassName("tabcontent");

    for(i = 0;i<tabContent.length;i++){
        tabContent[i].style.display = "none"; 
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(id_name).style.display = "block";
    e.currentTarget.className += " active";
}

$(document).on('submit','#openChat',function(e){
    e.preventDefault();
    window.location.href = '/chat/' + document.getElementById('openChat').classList[0]
})

document.getElementById("defaultOpen").click();