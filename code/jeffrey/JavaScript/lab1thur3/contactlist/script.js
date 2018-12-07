// objects
let workSpace = document.getElementById("container");

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

// function loops through the (key) array and assigns each element in the array into a prompt and asks for the value, puts into array
function getVals (arr){
  let list2 = [];
  for(element in arr){
      let input = prompt(`Input the ${arr[element]}:`);
      list2.push(input);
  }
  return list2;
}

// function loops through object extracting the keys into a list
function getKeys (object) {
  let list1 = [];
  for(let key in object) {
      list1.push(key);
      console.log(key);
  }
  return list1;
}

function newRecord () {
  let keys = getKeys(contacts_dict[0]);
  console.log(keys);
  console.log(contacts_dict);
  let set = document.createElement("div");

  set.style.display = "flex";
  set.style.justifyContent = "space-between";
  set.style.width = "100%";
  set.style.marginTop = "5px";

  keys.forEach(function(key) {
    let textbox;
    textBox = document.createElement("input");
    textBox.setAttribute("type", "text");
    textBox.setAttribute("placeholder", key);
    set.appendChild(textBox);
  });
  workSpace.appendChild(set);
}

// # List of CRUD FUNCTIONS BELOW
function create(){
  // let keys = getKeys(contacts_dict[0]);

  // let values = getVals(keys);

  // // creates a new object and blends the key.value pairs into an object
  // let result = {};
  // keys.forEach((key, i) => result[key] = values[i]);

  // checker = prompt(`Enter 'no if you don't want to add: ${result}`).toLowerCase();

  // if (checker != 'no'){
  //   contacts_dict.push(result);
  //   alert('Record created!');
  //   return contacts_dict;
  // }
  console.log("create");
  newRecord();
}

function retrieve(){
  let keys = getKeys(contacts_dict[0]);

  let input = prompt(`What is the ${keys[0]} of the record that you would like to retrieve? `);

  let result = contacts_dict.map(a => a.Name);

  if (result.includes(input) === true){
    for (i=0; i<contacts_dict.length; i++){
      if (input === contacts_dict[i].Name){
        alert(`Record: \n${contacts_dict[i].Name}\n${contacts_dict[i].FavoriteFruit}\n${contacts_dict[i].FavoriteColor}\n${contacts_dict[i].Age}`);
        return;
      }
    }
  }else {
    alert(`Record not found.`);
  }
}


// # def update():
function update(){
  let keys = getKeys(contacts_dict[0]);
  console.log(keys);
  let record = prompt(`What is the ${keys[0]} of the record that you would like to update?`);

  let attribute = prompt(`What is the attribute that you would like to set: "${keys[0]}", "${keys[1]}", "${keys[2]}", or "${keys[3]}"?`);

  let new_attribute = prompt(`What would you like to change the "${attribute}" to? `);

  if (keys.includes(attribute) === true) {
      for (i=0; i<contacts_dict.length;i++){
          if (record === contacts_dict[i][keys[0]]){
              contacts_dict[i][attribute] = new_attribute;
              return contacts_dict;
          }
      }
  }else {
    alert(`Attribute not found.`);
  }
}

// # def delete():
function deleteFunc(){
  let keys = getKeys(contacts_dict[0]);

  let record = prompt(`What is the ${keys[0]} of the record that you would like to delete?`);

  let result = contacts_dict.map(a => a.Name);

  if (result.includes(record) === true){

    for (i=0;i<contacts_dict.length;i++){
      if (record === contacts_dict[i][keys[0]]){
          contacts_dict.splice(i, 1);
      }
    }
    alert("Record deleted.");
  }else {
    alert("Record not found.")
  }
}

// while (true){
//   choice = prompt(`Welcome ${user_name}, you have four options for actions:\n1. 'create' for making a new record\n2. 'retrieve' for retreiving a record\n3. 'update' for updating a record\n4.  'delete' for deleting a record\nWhat would you like to do?`).toLowerCase();

//   if (choice === 'create') {
//     create();
//   }else if (choice === 'retrieve') {
//     retrieve();
//   }else if (choice === 'update') {
//     update();
//   }else if (choice === 'delete') {
//     deleteFunc();
//   }

//   end_prog = prompt('Input any key to do another action or "quit" to exit the program:').toLowerCase();

//   if (end_prog === 'quit'){
//       break;
//   }
// }

