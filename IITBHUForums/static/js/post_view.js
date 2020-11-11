
$(document).on('submit','#comment_form', function(e){
    var current_path =  window.location.href;
    e.preventDefault();
    $.ajax({
        type : 'POST',
        url : current_path,
        data : {
            'comment' : $('#new_comment').val(),
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            if(data.result == 'success'){
                var new_comment =  document.createElement("div");
                var text = document.createTextNode(data.new_comment);
                new_comment.appendChild(text);
                var comments = document.getElementById("comments");
                comments.appendChild(new_comment);
                $('#new_comment').val('');
            }else{
                // save for later
            }
        },
        error:function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});