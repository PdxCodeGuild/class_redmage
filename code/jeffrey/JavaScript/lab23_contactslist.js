// objects
let contacts_dict, user_name, keys, new_data, lines;

// # opens a CSV file with write capability and reads it to variable: lines while splitting it on each line
// with (open('contact_list.csv', 'r+') as file):
    lines = file.read().split('\n');

// # create a new dict to append to later
contacts_dict = [];

// # user the first line as header to create the keys for the dict
keys = lines[0].split(',');

// # loop through the lines adding the them to the dict under their appropriate keys starting after the header line (row)
for (i=0; i<lines.length;i++){
    // # splits each line based off the commas
    line = lines[i].split(',');
    // # creates a dict out of the keys and the line items so that the items at the index fit into the keys at the same index (it makes them friends and then they are added into a dict)
    entry = dict(zip(keys,line));
    // # add those mini-dict entries to the list
    contacts_dict.append(entry);
}


user_name = prompt(`What is your ${(keys[0])}?`);

// # List of CRUD FUNCTIONS BELOW
function create(){
    var checker, entry_str, user_val1, user_val2, user_val3;

    user_val1 = prompt(`Input the ${(keys[0])}: `);
    user_val2 = prompt(`Input the ${(keys[1])}: `);
    user_val3 = prompt(`Input the ${(keys[2])}: `);

    entry_str = (lower(user_val1),lower(user_val2),lower(user_val3));

    checker = prompt(`Enter 'no if you don't want to add: ${entry_str}`);

    if (lower(checker) != 'no'){
        entry = dict(zip(keys,entry_str));
        contacts_dict.append(entry);
        alert('Record created!');
        return contacts_dict;
    }
}


function retrieve(){
    var user_val1 = lower(prompt(`What is the ${keys[0]} of the record that you would like to retrieve? `));

    for (i=0; i<contacts_dict.length; i++){
        if (user_val1 == contacts_dict[i][keys[0]]){
            print(`\nRecord: ${contacts_dict[i]}\n`);
            return;
        }
    }
}


// # def update():
function update(){
    var record = lower(input(`What is the ${keys[0]} of the record that you would like to update?`));
    var attribute = lower(prompt(`What is the attribute that you would like to set: "{keys[0]}", "{keys[1]}", or "{keys[2]}"?`));
    var new_attribute = prompt(`What would you like to change the "${attribute}" to? `);
    if (attribute in keys){
        for (i=0; i<contacts_dict.length;i++){
            if (record == contacts_dict[i][keys[0]]){
                contacts_dict[i][attribute] = new_attribute;
                alert("Update complete!\n");
                return contacts_dict;
            }
        }
    }
}

// # def delete():
function deleteFunc(){
    var record = prompt(`What is the ${keys[0]} of the record that you would like to delete?`);

    for (i=0;i<contacts_dict.length;i++){
        if (record == contacts_dict[i][keys[0]]){
            contacts_dict.remove(contacts_dict[i]);
            alert("Record deleted.");
            return contacts_dict;
        }
    }
}

while (true){
    alert(contacts_dict)
    choice = prompt(`Welcome ${user_name}, you have four options for actions:\n1. 'create' for making a new record\n2. 'retrieve' for retreiving a record\n3. 'update' for updating a record\n4.  'delete' for deleting a record\nWhat would you like to do?`)
    if (choice.lower() == 'create') {
        create();
    }else if (choice.lower() == 'retrieve') {
        retrieve();
    }else if (choice.lower() == 'update') {
        update();
    }else if (choice.lower() == 'delete') {
        deleteFunc();
    }

    end_prog = prompt('Input any key to do another action or "quit" to exit the program:');

    if (end_prog.lower() == 'quit'){
        break;
    }
}

// # sending back to csv reverets and prints back the first operation to the csv:
new_data = [];
// #starts list with the keys
new_data.append(",".join(keys));
// #converts the values from every dict to a list
for (i=0; i<contacts_dict.length;i++){
    data_list = list(contacts_dict[i].values());
    data = ",".join(data_list);
    new_data.append(data);
}

// #formats the list to a string seperated by \n
new_data = "\n".join(new_data);

// with (open('contact_list.csv', "w") as file){
    // file.write(str(new_data));
// }