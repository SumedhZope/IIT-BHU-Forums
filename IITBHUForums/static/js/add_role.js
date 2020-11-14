$(document).on('submit', '#submit_form', function(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: window.location.href,
        data : {
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
            role : $('#input_role').val()
        },
        success: function(data){
            console.log('hello');
            document.getElementById('result').innerHTML  = data.message;
        },
        error: function() {
            
        }
    });
});
