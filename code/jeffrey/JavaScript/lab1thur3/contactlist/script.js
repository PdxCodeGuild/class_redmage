// objects
let workSpace1 = document.getElementById("container1");


let createBtn = document.getElementById("create");
let deleteBtn = document.getElementById("delete");
let retrieveBtn = document.getElementById("retrieve");
let updateBtn = document.getElementById("update");

createBtn.addEventListener("click", create);
deleteBtn.addEventListener("click", deleteFunc);
retrieveBtn.addEventListener("click", retrieve);
updateBtn.addEventListener("click", update);


// # create a new dict to append to later
let contacts_dict = [
    {
        Name: "Matthew",
        FavoriteFruit: "blackberries",
        FavoriteColor: "orange",
        Age: 23,
    },
    {
        Name: "Sam",
        FavoriteFruit: "pineapple",
        FavoriteColor: "blue",
        Age: 35,
    },
    {
        Name: "Jeffrey",
        FavoriteFruit: "banana",
        FavoriteColor: "violet",
        Age: 29,
    },
    {
        Name: "Ben",
        FavoriteFruit: "persimmon",
        FavoriteColor: "black",
        Age: 22,
    }
]

// function loops through object extracting the keys into a list
function getKeys (object) {
  let list1 = [];
  for(let key in object) {
      list1.push(key);
  }
  return list1;
}

function newRecord () {
  let keys = getKeys(contacts_dict[0]);
  let set = document.createElement("div");
  let submitBtn = document.createElement("input");
  submitBtn.setAttribute("type", "submit");
  submitBtn.setAttribute("class", "button");
  let clearBtn = document.createElement("button");
  clearBtn.setAttribute("type", "submit")
  clearBtn.innerHTML = "Clear";
  clearBtn.setAttribute("class", "button");
  let cancelBtn = document.createElement("button");
  cancelBtn.setAttribute("type", "submit");
  cancelBtn.innerHTML = 'Cancel';

  set.style.display = "flex";
  set.style.justifyContent = "space-between";
  set.style.width = "100%";
  set.style.marginTop = "5px";
  set.style.flexDirection = "column";

  keys.forEach(function(key) {
    let textBox = document.createElement("input");
    textBox.setAttribute("type", "text");
    textBox.setAttribute("placeholder", key);
    textBox.setAttribute("class", "createFields")
    set.appendChild(textBox);
  });
  set.appendChild(submitBtn);
  set.appendChild(cancelBtn);
  set.appendChild(clearBtn);
  workSpace1.appendChild(set);

  function storeNewRecord() {
    let createFields = document.getElementsByClassName("createFields");
    let result = {};
    for (let i=0; i<createFields.length; i++) {
      result[createFields[i].placeholder] = createFields[i].value;
    };

    contacts_dict.push(result);
  }

  function resetPage () {
    workSpace1.removeChild(set);
  }

  submitBtn.addEventListener("click", function(e) {
    storeNewRecord(e);
    resetPage(e);
  });
  cancelBtn.addEventListener("click", resetPage);
}

// # List of CRUD FUNCTIONS BELOW
function create(){
  if (workSpace1.children.length === 0) {
    newRecord();
  } else {
    // do nothing
  }
}

function retrieve(){
  if ( workSpace1.children.length === 0) {
    let keys = getKeys(contacts_dict[0]);
    let set = document.createElement("div");
    let submitBtn = document.createElement("input");
    submitBtn.setAttribute("type", "submit");
    submitBtn.setAttribute("class", "button");
    let clearBtn = document.createElement("button");
    clearBtn.setAttribute("type", "submit")
    clearBtn.innerHTML = "Clear";
    clearBtn.setAttribute("class", "button");
    let cancelBtn = document.createElement("button");
    cancelBtn.setAttribute("type", "submit");
    cancelBtn.innerHTML = 'Cancel';

    set.style.display = "flex";
    set.style.justifyContent = "space-between";
    set.style.width = "100%";
    set.style.marginTop = "5px";
    set.style.flexDirection = "column";

    keys.forEach(function(key) {
      let textBox = document.createElement("input");
      textBox.setAttribute("type", "text");
      textBox.setAttribute("placeholder", key);
      textBox.setAttribute("class", "createFields")
      set.appendChild(textBox);
    });
    set.appendChild(submitBtn);
    set.appendChild(cancelBtn);
    set.appendChild(clearBtn);
    workSpace1.appendChild(set);

    function printRecords() {
      let createFields = document.getElementsByClassName("createFields");
      let headache = function () {
        let x;
        for (let i=0; i<createFields.length; i++) {
          if (createFields[i].placeholder === "Name") {
            x = createFields[i].value;
            console.log(x);
            return x;
          }
        }
      }

      for (let i=0; i<contacts_dict.length; i++) {
        if (contacts_dict[i].Name.indexOf(headache()) >= 0) {
          let arr = Object.values(contacts_dict[i]);
          console.log(arr);
          let li = document.createElement("li");
          li.setAttribute("id", "demon")
          li.innerText = arr;
          workSpace1.appendChild(li);
        }
      }
    }

    function resetPage () {
      workSpace1.removeChild(set);
      for (i=workSpace1.children.length-1; i>=0; i--) {
        function removeElement(elementId) {
          // Removes an element from the document
          var element = document.getElementById(elementId);
          element.parentNode.removeChild(element);
        }
        removeElement("demon");
      }
    }

    submitBtn.addEventListener("click", function(e) {
      printRecords(e);
    });

    cancelBtn.addEventListener("click", resetPage);

    clearBtn.addEventListener("click:", clearForm);
  }else {
    // do nothting
  }
}


// # def update():
function update(){
  let keys = getKeys(contacts_dict[0]);
  let set = document.createElement("div");
  let submitBtn = document.createElement("input");
  submitBtn.setAttribute("type", "submit");
  submitBtn.setAttribute("class", "button");
  let clearBtn = document.createElement("button");
  clearBtn.setAttribute("type", "submit")
  clearBtn.innerHTML = "Clear";
  clearBtn.setAttribute("class", "button");
  let cancelBtn = document.createElement("button");
  cancelBtn.setAttribute("type", "submit");
  cancelBtn.innerHTML = 'Cancel';

  set.style.display = "flex";
  set.style.justifyContent = "space-between";
  set.style.width = "100%";
  set.style.marginTop = "5px";
  set.style.flexDirection = "column";

  keys.forEach(function(key) {
    let textBox = document.createElement("input");
    textBox.setAttribute("type", "text");
    textBox.setAttribute("placeholder", key);
    textBox.setAttribute("class", "createFields")
    set.appendChild(textBox);
  });
  set.appendChild(submitBtn);
  set.appendChild(cancelBtn);
  set.appendChild(clearBtn);
  workSpace1.appendChild(set);

  function printRecords() {
    let createFields = document.getElementsByClassName("createFields");
    let headache = function () {
      let x;
      for (let i=0; i<createFields.length; i++) {
        if (createFields[i].placeholder === "Name") {
          x = createFields[i].value;
          console.log(x);
          return x;
        }
      }
    }

    for (let i=0; i<contacts_dict.length; i++) {
      if (contacts_dict[i].Name.indexOf(headache()) >= 0) {
        let arr = Object.values(contacts_dict[i]);
        console.log(arr);
        let li = document.createElement("li");
        li.innerText = arr;
        workSpace1.appendChild(li);
      }
    }
  }

  function resetPage () {
    workSpace1.removeChild(set);
  }

  submitBtn.addEventListener("click", function(e) {
    printRecords(e);
  });

  cancelBtn.addEventListener("click", resetPage);

}

// # def delete():
function deleteFunc(){
  let keys = getKeys(contacts_dict[0]);
  let record = prompt(`What is the ${keys[0]} of the record that you would like to delete?`);

  let result = contacts_dict.map(a => a.Name);

  if (result.includes(record) === true){

    for (i=0;i<=contacts_dict.length;i++){
      if (record === contacts_dict[i][keys[0]]){
          contacts_dict.splice(i, 1);
      }
    }
    alert("Record deleted.");
  }else {
    alert("Record not found.")
  }
}