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
    const dropdown = document.querySelector('.dropdown')
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

const process = () =>{
    navSlide();
    dropdownUser();
}

process();