
const deck = document.getElementsByClassName('card_image');
const card_front = "static/images/snowflake-regular.svg";
const card_back1 = "static/images/socks-solid.svg";
const card_back2 = "static/images/anchor-solid.svg";
const card_back3 = "static/images/avianex-brands.svg";
const card_back4 = "static/images/bath-solid.svg";
const card_back5 = "static/images/canadian-maple-leaf-brands.svg";
const card_back6 = "static/images/cloud-sun-rain-solid.svg";
const card_back7 = "static/images/pagelines-brands.svg";
const card_back8 = "static/images/tree-solid.svg";
var img_array1 = [card_back1, card_back2, card_back3, card_back4, card_back5, card_back6, card_back7, card_back8];
var img_array2 = [card_back1, card_back2, card_back3, card_back4, card_back5, card_back6, card_back7, card_back8];
const deck_card_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen']
var card_img_obj = new Map();
// timer is for pausing the card flip on no-match
var timer;
var flipped_card = false;
var first_card;
var second_card;
var matches_found = 0;
var star_count = 0;
//     the stop-clock variables
var stop_clock = null;
var seconds = 0;
var minutes = 0;


function increment(){
  var time_element_seconds = document.getElementById("time_element_seconds");
  var time_element_minutes = document.getElementById("time_element_minutes");
  seconds += 1;
  if(seconds > 59){
    minutes += 1;
    seconds = 0;
  }

  time_element_minutes.innerHTML = minutes;
  time_element_seconds.innerHTML = seconds;
  //alert(time_element_seconds);
};


function stars(){
  if(star_count > 3){
    //pass
  }
  else if(star_count == 3){
    star = document.getElementById('star3');
    star.style.color = 'blue';
  }
  else if(star_count == 2){
    star = document.getElementById('star2');
    star.style.color = 'blue';
  }
  else if(star_count == 1){
    star = document.getElementById('star1');
    star.style.color = 'blue';
  }
  else{
      star1 = document.getElementById('star3');
      star2 = document.getElementById('star2');
      star3 = document.getElementById('star1');
      star1.style.color = 'black';
      star2.style.color = 'black';
      star3.style.color = 'black';
  }
};

function congrats(){
  var element = document.getElementById("winner")
  var message = "<br>You win!<br>"
  element.innerHTML = message;
};

function clear_congrats(){
  var element = document.getElementById("winner")
  var message = ""
  element.innerHTML = message;

}

function flip_card(){
  //alert("card flipped, event listener active");

  var card_id = this.id;
  var new_src = card_img_obj.get(card_id);
  if(!flipped_card){
  this.src = new_src.toString();
  flipped_card = true;
  first_card = new_src;
  }
  else if(flipped_card){
    this.src = new_src.toString();
    second_card = new_src;
    if(first_card === second_card){
      flipped_card = false;
      matches_found += 1;
      star_count += 1;
      stars()
      if(matches_found >= 8){
        congrats()
        clear_clock();

      }
    }
    else{

      flipped_card = false;
      matches_found = 0;
      star_count = 0;
      stars();
      timer = window.setInterval(reset_flip, 1000);

    }
  }
};

function assign_imgs(imgArray1, imgArray2, card_map, deck){
  var indeck = 0;
  //assign first shuffled images to map
  for (var i = 0; i<imgArray1.length; i++){
    var img_to_add = imgArray1[i];
    var card_to_add_it_to = deck[indeck];
    card_map.set(card_to_add_it_to, img_to_add);
    indeck += 1;
    //alert(indeck);
  };
  //assign second shuffled images to map
  for (var i = 0; i<imgArray2.length; i++){
    var img_to_add = imgArray2[i];
    var card_to_add_it_to = deck[indeck];
    card_map.set(card_to_add_it_to, img_to_add);
    indeck += 1;
    //alert(indeck);
  };
}


function shuffleArray(array) {
   //https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
   //  the Durstenfeld shuffle
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    };
}



function reset_flip(){
  if(seconds > 0){
    // this set interval waits 1 second for flip so adjust seconds -1
  seconds -= 1;
  }
  window.clearInterval(timer);
  flipped_card = false;
  first_card = "";
  second_card = "";
  for (let i=0; i<deck.length; i++){
    let element = deck[i];
    //alert(i);
    element.src = card_front;
    };
;}


function clear_clock(){
  if(stop_clock != null){
    window.clearInterval(stop_clock);
  }
  seconds = 0;
  minutes = 0;
};

function run_game(){
  star_count = 0;
  stars();
  clear_clock();
  clear_congrats();
  flipped_card = false;
  for (let i=0; i<deck.length; i++){
    let element = deck[i];
    element.addEventListener("click", flip_card);
    element.src = card_front;
  };
  shuffleArray(img_array1);
  shuffleArray(img_array2);
  assign_imgs(img_array1, img_array2, card_img_obj, deck_card_names);
  stop_clock = window.setInterval(increment, 1000);

};
