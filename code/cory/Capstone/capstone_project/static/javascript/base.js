let hamburger = document.getElementById("hamburger");
let menu = document.getElementById("menu");

hamburger.addEventListener("click", function(e) {
    hamburger.classList.toggle("is-active");
    menu.classList.toggle("is-active")
});


let menuOptions = document.getElementsByClassName("menu-option");

for (i = 0; i < menuOptions.length; i++) {
    menuOptions[i].addEventListener("click", function(e) {
        hamburger.classList.toggle("is-active");
        menu.classList.toggle("is-active")
    });
};