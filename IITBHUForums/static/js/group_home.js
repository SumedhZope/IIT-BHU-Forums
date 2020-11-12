let w1 = 0,
    w2 = 0,
    w3 = 0;
$(document).ready(function resize() {
    // your code
    w1 = $(".imgGroup").width();
    w2 = $(".uperwalacard").width();
    w3 = w2 - w1 - 30;
    let s = w3.toString() + 'px';
    $('.upper_right').css('width', s);
});

function liked() {
    if ($('#like').attr('src') == '/static/img/liked.png') {
        $('#like').attr('src', '/static/img/heart.png');
        let x = $('#no_likes').html();
        let y = parseInt(x) - 1;
        $('#no_likes').html(y);
        $.ajax({
            type: 'POST',
            url: '.',
            data: {
                'like': y,
                'val': 'dec',
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            cache: false,
        });
    } else {
        $('#like').attr('src', '/static/img/liked.png');
        let x = $('#no_likes').html();
        let y = parseInt(x) + 1;
        $('#no_likes').html(y);
        $.ajax({
            type: 'POST',
            url: '.',
            data: {
                'like': y,
                'val': 'inc',
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            cache: false,
        });
    }
}