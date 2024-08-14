
// LISTENING TO MENU BUTTON CLICKS TO OPEN NAVBAR
// LISTENING TO OVERLAY CLICKS TO CLOSE NAVBAR

document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector(".nav");
  const navLinks = document.querySelectorAll(".nav__link");

  document.querySelector("#btnNav").addEventListener("click", () => {
    nav.classList.add("nav--open");
  });

  document.querySelector(".nav__overlay").addEventListener("click", () => {
    nav.classList.remove("nav--open");
  });

  // Add an event listener to each navigation link to close the navbar
  navLinks.forEach((navLink) => {
    navLink.addEventListener("click", () => {
      nav.classList.remove("nav--open");
    });
  });
});
