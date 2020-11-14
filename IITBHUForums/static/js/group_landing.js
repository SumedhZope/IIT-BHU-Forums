$(document).ready(() => {
    join_func();
    let x = document.getElementsByClassName('card-text');
    //console.log(x[0].innerHTML);
    for (var i = 0; i < x.length; i++) {
        let str = x[i].innerHTML;
        //console.log(str);
        if (str.length > 28) {
            x[i].innerHTML = str.slice(0, 28);
        }
    }
})

const join_func = () => {
    btn = document.getElementsByClassName('join-btn');
    Array.from(btn).forEach(element => {
        element.addEventListener('click', e => {
            var current_path =  window.location.href;
            element.innerHTML = "Joined";
            $.ajax({
                type : 'POST',
                url : current_path,
                data : {
                    'group_id' : element.id, 
                    'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
                },
            });
        })
    })
}