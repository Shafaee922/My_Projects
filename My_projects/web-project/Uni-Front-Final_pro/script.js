// Start header
const toggle = document.getElementById('menu-toggle');
  const nav = document.getElementById('nav');

  toggle.addEventListener('click', () => {
    nav.classList.toggle('active');
  });

// Header Main Page 
window.addEventListener("scroll", () => {
    const header = document.querySelector(".header-main");
    const scrollY = window.scrollY;

    if (scrollY > 50) {
      header.style.backgroundImage =
        `linear-gradient(to right bottom, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('../images/header-bg.jpg')`;
    } else {
      header.style.backgroundImage =
        `linear-gradient(to right bottom, rgba(41, 39, 39, 0.4), rgba(74, 72, 72, 0.4)), url('../images/header-bg.jpg')`;
    }
  });