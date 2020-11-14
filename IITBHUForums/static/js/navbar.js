const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.ul-1')
    
    burger.addEventListener('click',() => {
        nav.classList.toggle('nav-active');
        burger.classList.toggle('toggle');
    })


}

const dropdownUser = () =>{
    const triangle = document.querySelector('.triangle');
    const user = document.querySelector('.user');
    const profile_picture = document.querySelector('.profile-picture');
    const dropdown = document.querySelector('.dropdown');
    triangle.addEventListener('click',() => {
        dropdown.classList.toggle('dropdown-active');
        triangle.classList.toggle('triangle-active');
        profile_picture.classList.toggle('profile-picture-active');
    });
    user.addEventListener('click',() => {
        dropdown.classList.toggle('dropdown-active');
        triangle.classList.toggle('triangle-active');
        profile_picture.classList.toggle('profile-picture-active');
    });
    profile_picture.addEventListener('click',()=> {
        dropdown.classList.toggle('dropdown-active');
        triangle.classList.toggle('triangle-active');
        profile_picture.classList.toggle('profile-picture-active');
    });
}

const searchbar = () => {
    const search = document.querySelector('.search');
    const searchimage = document.querySelector('.search-image');
    const searchinput = document.querySelector('.search-input');
    searchimage.addEventListener('click',() => {
        search.classList.toggle('search-active');
        searchimage.classList.toggle('search-image-active');
        searchinput.classList.toggle('search-input-active');
    });

}

window.onclick = function(event){
    const triangle = document.querySelector('.triangle');
    const dropdown = document.querySelector('.dropdown');
    const dropdown_main_div = document.querySelector('.ul-2');
    const profile_picture = document.querySelector('.profile-picture');

    if(event.target != dropdown && event.target.parentNode != dropdown && event.target != dropdown_main_div && event.target.parentNode != dropdown_main_div && event.target != profile_picture){
        triangle.classList.remove('triangle-active');
        dropdown.classList.remove('dropdown-active');
    }
}

const validateForm = () => {
    const input = document.getElementById('search_bar');
    const form = document.getElementById('search_form')
    if(input.value.length == 0){
        return false;
    }
}
const process = () =>{
    navSlide();
    dropdownUser();
    searchbar();
}

process();

