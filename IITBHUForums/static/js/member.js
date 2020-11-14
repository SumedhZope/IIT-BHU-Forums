const submit_role_form = function(e){
    btn_list = document.getElementsByClassName('submit-form-btn');
    Array.from(btn_list).forEach(element => {
        element.addEventListener('click',e => {
            e.preventDefault();
            $.ajax({
                type: 'POST',
                url: window.location.href,
                data: {
                    'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
                    'new_role' : document.getElementById(element.id + '_newrole').value,
                    'user_id' : element.id
                },
                success: function() {
                    console.log('done')
                }
            });
        })
    });
}

submit_role_form();