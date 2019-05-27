//Javascript for NIM game ex5

const firstRow = ["one"];
const secondRow = ["two", "three", "four"];
const thirdRow = ["five", "six", "seven", "eight", "nine"];
const fourthRow = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen"];
cpu_choices = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen"];
player_row = null;

function instructions(){
  let message1 = "A player will pick a row of cards to choose from on their turn.   ";
  let message2 = "They can choose to remove one, or up to all cards in the row.   ";
  let message3 = "Player only gets to choose from one row on their turn.";
  let message4 = "Once the 'END TURN' button is clicked, the next user can select their choices.";
  let message5 = "next player follows the same rules.";
  let message6 = "Player left with last card on board as choice is the loser.  ";
  alert(message1 + message2 + message3 + "\n" + message4 + "\n" + message5 + message6);
};


function check_hidden(choice){
  var element = document.getElementById(choice);

  if(element.style.visibility === "hidden"){
    //pass
  }
  else{
    element.style.visibility = "hidden";
  }
};


function get_active_row(item){
  //alert(item);

  if(firstRow.includes(item)){

    return firstRow;
  }
  else if(secondRow.includes(item)){


    return secondRow;
  }
  else if(thirdRow.includes(item)){


    return thirdRow;
  }
  else if(fourthRow.includes(item)){

    return fourthRow;
  }
  else{
    return null;
  }
};


function validate_row(item){
  let row = get_active_row(item);
  if(player_row !== null){
    if(player_row.includes(item)){
      return true;
    }
    else{
      return false;
    }
  }
  else{
    player_row = get_active_row(item);
    return true;
  }

};


function get_row(item){
  //alert(item);
  let valid = validate_row(item);
  //alert(valid);
  if(valid){
  check_hidden(item);
  }
  else{
    alert("choices must be from the same row");
  }
};


function cpu_turn(){
  player_row = null;
  //make a choice from a row
  //pause
  //complete
  //pause
  alert("next human's turn");
}
