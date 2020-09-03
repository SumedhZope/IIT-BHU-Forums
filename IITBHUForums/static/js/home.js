$(document).ready(function(){
    resposive();
});
$(window).resize(function(){
    resposive();
});

function resposive(){
    var h = $(window).height()-$('.header').height()-$('.front').height();
    h /= 2;
    $('.front').css({'padding-top':h+'px'});
}


