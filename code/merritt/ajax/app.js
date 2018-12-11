let target = document.getElementById("target");
let btn = document.getElementById("btn-dog");

btn.addEventListener("click", function(e) {
  let req = new XMLHttpRequest();

  req.addEventListener("progress", function(e) {
    target.innerText = `Request ${ e.loaded / e.total * 100 }% complete.`
  });

  req.addEventListener("error", function(e) {
    target.innerText = `${req.statusText} ${req.status}`
    console.log(req);
  });

  req.addEventListener("load", function(e) {
    let response = JSON.parse(req.responseText);
    console.log(req.responseText);
    console.log(response);
    response.forEach(function(dog) {
      let li = document.createElement("li");
      li.innerText = `${dog.name} is a ${dog.good} dog! Age of ${dog.age}.`;
      target.appendChild(li);
    });
  });

  req.open("GET", "ajax.json");
  req.send()
});