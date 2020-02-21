// JS code for hamburger icon

let noodle_nav;
let hamburg;


function set_DOM() {
    noodle_nav = document.getElementById("nav_link_menu")
    hamburg = document.getElementById("hamburg")
}

function show(element) {
    element.style.display = 'flex';
}

function hide(element) {
    element.style.display = 'none';
}

function toggle_burger() {
    current = hamburg.getAttribute("value")
    if (current == "ON") {
        hamburg.setAttribute("value", "OFF")

        hide(noodle_nav)
    }
    else {
        hamburg.setAttribute("value", "ON")

        show(noodle_nav)
    }

}


function set_listener() {
    hamburg.addEventListener('click', toggle_burger)
}

window.addEventListener('load', (event) => {
    set_DOM();
    set_listener();
});
