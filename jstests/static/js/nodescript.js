// JavaScript file

var whsp13 = "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp";
var whsp9 = "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp";
var whsp6 = "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp";
var whsp3 =  "&nbsp&nbsp&nbsp";
var text1 = "--====[]====--";
var text1a ="|=-----------=|";
var text1b ="|" + whsp13 + "|";
var text2 = "|[" + whsp3 + "]=|=[" + whsp3 + "]|";
var text3 = "|[" + whsp3 + "]=|=[" + whsp3 + "]|";
var text4 = "|" + whsp6 + "|" + whsp6 + "|";
var text4a = "|" + whsp6 + "|" + whsp6 + "|";
var text4b = "|" + whsp6 + "|" + whsp6 + "|";
var text4c = "|" + whsp6 + "|" + whsp6 + "|";
var text5 = "|______+______|";
var alist = [text1, text1a, text1b, text2, text3, text4, text4a, text4b, text4c, text5];
var topmarginlist = ['50px', '100px', '150px', '200px', '300px'];
var place_of_margin_top = 0;
var leftpaddinglist = ['100px', '200px', '300px', '400px', '500px'];
var place_of_padding_left = 0;

function doSomething(){

  var texta = ' ';
  x = alist.length
  for (i = 0; i < x; i++) {
    newtext = alist[i];
    texta += newtext + "<br>";
  }
  x = topmarginlist[place_of_margin_top];
  document.getElementById("tardisbox").style.marginTop = x;
  y = leftpaddinglist[place_of_padding_left];
  document.getElementById("tardisbox").style.paddingLeft = y;
  document.getElementById("tardisbox").innerHTML = texta;
  //alert("function doSomething() activated");

}


function move_down(){
  start = document.getElementById("tardisbox").style.marginTop;
  if(start == "10px"){
    //doSomething handles it
    place_of_margin_top = 0;
  }
  else if (place_of_margin_top > 4){
    //pass -- no where to go
  }
  else{
    // increment padding
    place_of_margin_top += 1;
  }
  doSomething();
}

function move_right(){
  start = document.getElementById("tardisbox").style.paddingLeft;
  if(start == "10px"){
    //start point, doSomething handles move/render
    //pass
  }
  else if (place_of_padding_left > 4){
    //pass -- no move
  }
  else{
    //increment margin -- move
    place_of_padding_left += 1;
  }
  //render text to screen
  doSomething();
}


function move_up(){
  start = document.getElementById("tardisbox").style.marginTop;
  if(start == "10px"){
    //pass
  }
  else if (place_of_margin_top > 0){
    //increment margin back
    place_of_margin_top -= 1;
  }
  else{
   //pass no move
  }
  doSomething();
}



function move_left(){
  start = document.getElementById("tardisbox").style.paddingLeft;
  if(start == "10px"){
    //pass
  }
  else if (place_of_padding_left <= 0){
    // pass no move
  }
  else{
    place_of_padding_left -= 1;
  }
  doSomething();

  }



function reset(){


  document.getElementById("tardisbox").style.marginTop = "10px";
  document.getElementById("tardisbox").style.paddingLeft = "10px";
  place_of_margin_top = 0;
  place_of_padding_left = 0;
  var texta = ' ';
  x = alist.length
  for (i = 0; i < x; i++) {
    newtext = alist[i];
    texta += newtext + "<br>";
  }
  document.getElementById("tardisbox").innerHTML = texta;
}


window.onload = function(){
  document.getElementById("clickme").addEventListener("click", doSomething);
  document.getElementById("moveright").addEventListener("click", move_right);
  document.getElementById("movedown").addEventListener("click", move_down);
  document.getElementById("moveleft").addEventListener("click", move_left);
  document.getElementById("reset").addEventListener("click", reset);
  document.getElementById("moveup").addEventListener("click", move_up);
}
