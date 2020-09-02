const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.ul-1')
    
    burger.addEventListener('click',() => {
        nav.classList.toggle('nav-active');
        burger.classList.toggle('toggle');
    })


    console.log("run");
}

const dropdownUser = () =>{
    const triangle = document.querySelector('.triangle');
    const dropdown = document.querySelector('.dropdown')
    triangle.addEventListener('click',() => {
        dropdown.classList.toggle('dropdown-active');
        triangle.classList.toggle('triangle-active')
    })
}

const process = () =>{
    navSlide();
    dropdownUser();
}

process();