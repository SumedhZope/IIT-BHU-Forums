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
                var text = document.createTextNode(data.user + " said : ");
                new_comment.appendChild(text);
                var br_tag = document.createElement("br");
                new_comment.appendChild(br_tag);
                text = document.createTextNode(data.new_comment);
                new_comment.appendChild(text);
                var comments = document.getElementById("comments");
                comments.prepend(new_comment);
                var num = document.getElementById('num');
                console.log(num.innerHTML);
                num.innerHTML = parseInt(num.innerHTML) + 1;
                $('#new_comment').val('');
            }
        },
        error:function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});