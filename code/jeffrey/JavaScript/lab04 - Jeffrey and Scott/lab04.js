let listbox = document.getElementById("container");
let btn;



btn = document.getElementById("createnew");

btn.addEventListener("click", newItem);

function newItem() {
    let todoItem;
    let checkBox;
    let textBox;
    let deleteButton;

    todoItem = document.createElement("div");
    todoItem.style.display = "flex";
    todoItem.style.justifyContent = "space-between";
    todoItem.style.width = "100%";
    todoItem.style.marginTop = "5px";

    checkBox = document.createElement("input");
    checkBox.setAttribute("type", "checkbox");
    checkBox.addEventListener("change", strikeThrough);

    textBox = document.createElement("input");
    textBox.style = "textbox";
    textBox.size = "120";
    textBox.addEventListener("keypress", function(e) {
        if (e.keyCode === 13) {
            newItem();
        }
    });
    

    deleteButton = document.createElement("button");
    deleteButton.innerText = "X";

    deleteButton.onclick = function() {
        this.parentElement.remove();
    };

    todoItem.appendChild(checkBox);
    todoItem.appendChild(textBox);
    todoItem.appendChild(deleteButton);
    listbox.appendChild(todoItem);
    textBox.focus();

    function strikeThrough() {
        if (checkBox.checked = true) {
            textBox.className += "strike-through";
        } else if (checkBox.checked = false) {
            textBox.className = "";
        }
    };
};

