// JavaScript source code for speech experiment

//const speech_div;
/*
var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList
var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent
let recognition = new SpeechRecognition();
*/
function get_line(element) {
    let line = element.innerHTML
    return line;

};

/*
function startREC(){
  recognition.start()
}
*/


/*
recognition.onresult = function(event) {
  // The SpeechRecognitionEvent results property returns a SpeechRecognitionResultList object
  // The SpeechRecognitionResultList object contains SpeechRecognitionResult objects.
  // It has a getter so it can be accessed like an array
  // The first [0] returns the SpeechRecognitionResult at the last position.
  // Each SpeechRecognitionResult object contains SpeechRecognitionAlternative objects that contain individual results.
  // These also have getters so they can be accessed like arrays.
  // The second [0] returns the SpeechRecognitionAlternative at position 0.
  // We then return the transcript property of the SpeechRecognitionAlternative object
  let textELEM = document.getElementById('sp2txt')
  let text = event.results[0][0].transcript;
  textELEM.innerHTML = text
}

recognition.onspeechend = function() {
  recognition.stop();
}




recognition.onerror = function(event) {
  diagnostic.textContent = 'Error occurred in recognition: ' + event.error;
}

*/

function addEventlistener_topage() {
    console.log("adding event listeners");
    let element = document.getElementById("js_say_word");
    let word_val = document.getElementById("word_to_say").innerHTML
    if(!word_val){
        word_val = "No word found."
    }
    element.addEventListener("click", function(){speak(word_val)}, false)
    let definition = document.getElementById("js_say_definition")
    let def_val = document.getElementById("definition_to_say").innerHTML
    if(!def_val){
        def_val = "No definition found."
    }
    definition.addEventListener("click", function(){speak(def_val)}, false)
}

function speak(line) {

    let utterance = new SpeechSynthesisUtterance(line);

    speechSynthesis.speak(utterance);
}

window.addEventListener('load', (event) => {

    addEventlistener_topage()
});