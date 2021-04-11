const hum = document.querySelector('.header .nav-bar .nav-list .hum');
const mobile_menu = document.querySelector('.header .nav-bar .nav-list ul');
const header = document.querySelector('.header.container');
const lheader = document.querySelector('#header');

hum.addEventListener('click', () => (
    hum.classList.toggle('active'),
    mobile_menu.classList.toggle('active')
));

document.addEventListener('scroll', () => {
    var scroll_position = window.scrollY;
    if (scroll_position > 250) {
        // header.style.backgroundColor = "#29323c";
        lheader.style.backgroundColor = "white";
    } else {
        // header.style.backgroundColor = "transparent";
        lheader.style.backgroundColor = "white";
    }
});