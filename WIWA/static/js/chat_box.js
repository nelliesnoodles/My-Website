//JavaScript file for whispering wall (Wiwa)'s chat box


function store_words(which){
  var user_words = document.getElementById("user_words").value;
  var wiwa_words = document.getElementById("wiwa_words").value;
  var chat_log = localStorage.getItem('chat_log');

  if(chat_log === null){

    localStorage.setItem('chat_log', "<br>");

  }
  else{

    if(which == 'user_words'){
      var user_words = document.getElementById("user_words").value;
      let words = "<b>user</b>:" + user_words + "<br>";
      localStorage.setItem('chat_log', chat_log + words);
    }
    if(which === 'wiwa_words'){
      var user_words = document.getElementById("wiwa_words").value;
      //console.log("which=wiwa, words=", user_words)
      //If wiwa response is an empty string, she is not sending a response, GET was not intended for her.
      //TODO: fix the Django views to ignore GET requests not involving user_input sumbit clicks.
      if (user_words != ''){
          let words = "<b>wiwa</b>:<i>" + wiwa_words + "<br></i>";
          localStorage.setItem('chat_log', chat_log + words);
      }
    }
  }
};


function clear_storage(){
  var chatbox = document.getElementById('chatbox');
  localStorage.clear();
  localStorage.setItem('chat_log', "<br>");
  chatbox.innerHTML = "chat screen cleared";

};

function scroll_to_bottom(){
  var objDiv = document.getElementById("chatbox");
  objDiv.scrollTop = objDiv.scrollHeight;
};

window.onload = function(){
  store_words('wiwa_words');
  var chat_log = localStorage.getItem('chat_log');
  var element = document.getElementById("chatbox");
  //alert(element);
  var linebreak = document.createElement("br");
  if(typeof element !== 'undefined' && element !== null) {
    element.innerHTML += chat_log;
    }
  scroll_to_bottom();
};
