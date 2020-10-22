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
                window.location.href = '..';
            } else {
                // $('#new_group_error').css({ 'display': 'block' });
                $('#new_group_error').html(data.message);
            }
        },
        error: function() {
            contact_right_message_sent.text('Sorry! Something went wrong.')
        }
    });
});