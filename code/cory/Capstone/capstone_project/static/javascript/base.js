let hamburger = document.getElementById("hamburger");

let menu = document.getElementById("menu")

hamburger.addEventListener("click", function(e) {
    hamburger.classList.toggle("is-active");
    menu.classList.toggle("is-active")
});