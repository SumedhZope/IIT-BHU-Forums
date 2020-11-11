$(document).on('submit', '#submit', function(e) {
    e.preventDefault();
    var formData = new FormData(this);
    console.log(formData);
    $.ajax({
        type: 'POST',
        url: '.',
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function(data) {
            if (data.result == 'success') {
                window.location.href = '/groups/';
            } else {
                $('#new_group_error').html(data.message);
            }
        },
        error: function() {
            contact_right_message_sent.text('Sorry! Something went wrong.');
        }
    });
});

//function file() {
//  console.log($('#g_file').val());
// var x = $('#g_file').val();
//}