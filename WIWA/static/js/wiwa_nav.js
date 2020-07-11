
function watch_burg(){

    let element = document.getElementById("hamburg")
    console.log(`element = ${element}`)
    let state = element.getAttribute('value')
    let links = document.getElementById("nav_link_menu")
    if(state === 'OFF'){
        links.style.display = 'none';
    }
    if(state === 'ON'){
        links.style.display = 'flex';
    }

}

function listen_click(){
    let element = document.getElementById("hamburg")
    let state = element.getAttribute('value')
    let links = document.getElementById("nav_link_menu")
    console.log(`state value = ${state}`)
    if(state == 'OFF'){
        console.log('altering display=ON')
        links.style.display = 'flex';
        element.setAttribute('value', 'ON');
    }
    if(state == 'ON'){
        console.log('altering display=OFF')
        links.style.display = 'none';
        element.setAttribute('value', 'OFF');
    }

}


window.addEventListener('load', (event) => {
    watch_burg()

});