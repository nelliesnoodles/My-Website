//JavaScript file for whispering wall (Wiwa)'s chat box
/*  NOTES:
Html contains two id='wiwa_words', id="wiwa_words1" one is for testing.  It is
currently commented out. The element that is used to append conversation
to the chatbox, we need the element.value
the element for testing, her words are element.innerHTML



*/

function store_user(){
    let user_words = document.getElementById("user_words").value;
    let chat_log = localStorage.getItem('chat_log');
    let words = ''
    if(chat_log === null){
    //  console.log('null clause')

    localStorage.setItem('chat_log', "<br>");

   }
   else{
       if(user_words != ''){
           user_words = document.getElementById("user_words").value;
           words = "<b>user</b>:" + user_words + "<br>";
           localStorage.setItem('chat_log', chat_log + words);

       }
   }
   //console.log(chat_log)


}


function store_wiwa(){

  let wiwa_words = document.getElementById("wiwa_words").value;
  let chat_log = localStorage.getItem('chat_log');
  let words = ''

  if(chat_log === null){

    localStorage.setItem('chat_log', "<br>");

  }
  else{


    if(wiwa_words){



          words = "<b>wiwa</b>:<i>" + wiwa_words + "<br></i>";

          localStorage.setItem('chat_log', chat_log + words);

    }
  }
};

function scroll_to_bottom(){
  let objDiv = document.getElementById("chatbox");
  objDiv.scrollTop = objDiv.scrollHeight;
};



function clear_storage(){
  let chatbox = document.getElementById('chatbox');
  localStorage.clear();
  localStorage.setItem('chat_log', "<br>");
  chatbox.innerHTML = "chat screen cleared";

};

function scroll_to_bottom(){
  let objDiv = document.getElementById("chatbox");
  objDiv.scrollTop = objDiv.scrollHeight;
};

function set_chatbox(){
  store_wiwa();
  let chat_log = localStorage.getItem('chat_log');
  let words = '';
  let chatbox = document.getElementById('chatbox');


  if(chat_log === null){
      console.log('null clause')

    localStorage.setItem('chat_log', "<br>");

  }
  else{
      chatbox.innerHTML = chat_log
      scroll_to_bottom();

  }


}

window.addEventListener('load', (event) => {
    set_chatbox();




});




