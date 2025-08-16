const burger = document.querySelector('.rise-burger');
const navLinks = document.querySelector('.rise-nav-links');

burger.addEventListener('click', () => {
    burger.classList.toggle('open');
    navLinks.classList.toggle('active');
});
