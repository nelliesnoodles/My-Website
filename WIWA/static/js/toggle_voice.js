// toggle switch
// localStorage.setItem('myCat', 'Tom');
// localStorage.getItem('myCat');

function toggle(){
    let toggleSwitch = document.getElementById("myonoffswitch")
    let current = localStorage.getItem('voice')
    if(current == null){
        localStorage.setItem('voice', 'OFF')
    }
    else {

        if(toggleSwitch !== undefined && toggleSwitch !== null){
            let value = toggleSwitch.getAttribute('value');
            if(value == 'ON'){
                toggleSwitch.setAttribute('value', 'OFF')
                toggleSwitch.innerHTML ='Voice: OFF'
                localStorage.setItem('voice', 'OFF')
            }
            else {
                toggleSwitch.setAttribute('value', 'ON')
                localStorage.setItem('voice', 'ON')
                toggleSwitch.innerHTML = 'Voice: ON'
            }
        }
    }
}
