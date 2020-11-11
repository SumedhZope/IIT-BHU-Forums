$(document).ready(() => {
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