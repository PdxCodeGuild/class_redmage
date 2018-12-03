// To do list

let addItem = document.getElementById("add-item")
let addBtn = document.getElementById("add-btn")
let items = document.getElementById("items")

function newItem() {
    let newEntry = addItem.value;
    let listItem = document.createElement("li");
    let checkbox = document.createElement("input");
    checkbox.setAttribute("type", "checkbox");
    listItem.appendChild(checkbox);
    listItem.appendChild(document.createTextNode(newEntry));
    items.appendChild(listItem);
    addItem.value = "";
    checkbox.addEventListener("change",function(){
        if (this.checked) { 
            let done = listItem.strike();
            this.innerHTML = done;
        }else {
        }
    });
}

addBtn.addEventListener("click", newItem);