let array, destination, random, count, countdown;


count = 5;

countdown = function(){
  document.getElementById("target").innerHTML = count;
  count--;
  // console.log(count);
  if (count === 0){
    setTimeout(redirect, 1000);
  }
}
// console.log(count);


array = ["https://www.google.com/", "https://www.yahoo.com/", "https://www.comcast.com/", "https://www.etrade.com/","https://www.pornhub.com/"];

random = Math.random();
// console.log(random);

destination = array[Math.round(random*array.length)]

function redirect (){
  // another way to redirect is to use location.assign()
  location.assign(destination);
  // window.location = destination;
}

setInterval(countdown, 1000);