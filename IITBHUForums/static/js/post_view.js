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
                var new_br_tag = document.createElement("br");
                comments.prepend(new_br_tag);
                comments.prepend(new_comment);
                var num = document.getElementById('num');
                num.innerHTML = parseInt(num.innerHTML) + 1;
                $('#new_comment').val('');
            }
        },
        error:function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});

const like_btn = () => {
    btn = document.getElementById('like_btn');
    console.log(btn)
    num = document.getElementById("likes_num")
    btn.addEventListener('click', e =>{
        if(btn.classList.contains("like-active")){
            num.innerHTML = parseInt(num.innerHTML) - 1;
            btn.classList.remove("like-active")
            $.ajax({
                type : 'POST',
                url : window.location.href,
                data : {
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
                    like : "delete"
                }
            });
        }
        else{
            num.innerHTML = parseInt(num.innerHTML) + 1;
            btn.classList.add("like-active")
            $.ajax({
                type : 'POST',
                url : window.location.href,
                data : {
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
                    like : "create"
                }
            });
        }
    });
}
like_btn();