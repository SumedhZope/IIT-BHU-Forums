$(document).ready(function(){
    resposive();
});
$(window).resize(function(){
    resposive();
});

function resposive(){
    var h = $(window).height()-$('.header').height();
    //console.log(h);
   // $('.front').css({'height':h+'px'});
    if(screen.width<800){
        $('.content').css({'display':'block'});
        $('.loading_img').css({'width':'70%'});
        $('.logo').css({'max-height':'150px'});
        $('.sign').css({'height':'130px'});
        $('.sign').css({'font-size':'40px'});
        $('.content_child').css({'width':'100%'});
    }else if(screen.width<1415){
        $('.content').css({'display':'flex'});
        $('.loading_img').css({'width':'80%'});
        $('.logo').css({'max-height':'100px'});
        $('.sign').css({'height':'100px'});
        $('.sign').css({'font-size':'30px'});
        $('.content_child').css({'width':'50%'});
    }else{
        $('.content').css({'display':'flex'});
        $('.loading_img').css({'width':'60%'});
        $('.logo').css({'max-height':'100px'});
        $('.sign').css({'height':'100px'});
        $('.sign').css({'font-size':'30px'});
        $('.content_child').css({'width':'50%'});
    }
}
