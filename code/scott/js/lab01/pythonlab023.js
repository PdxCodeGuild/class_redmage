// lab23_contacts.py

var contacts = [
    {
        name: 'matthew',
        favoriteFruit: 'blackberries',
        favoriteColor: 'orange'
    },
    {
        name: 'sam',
        favoriteFruit: 'pineapple',
        favoriteColor: 'blue' 
    }
]

// Version 2
// function to return a formatted entry - can be called by create or edit functions
function createContact(contacts) {
    let invalidInput = true; 
    while (invalidInput = true) {
        let input_name = prompt("Please enter the name of the contact to create. ");
        let favColor = prompt("Enter the favorite color. ")
        let favFruit = prompt("Enter the favorite fruit. ")
        let createConf = prompt(`Your entry shows ${input_name} loves ${fav_fruit} and the color ${fav_color}. Correct('Y' or 'N')? `)
        createConf = createConf.toUpperCase;
        if (createConf === "Y") {
            let contact = {
                name: input_name,
                favoriteColor: fav_color,
                favoriteFruit: fav_fruit
            }
            contacts.push(contact);
            return contacts;
        } else if (create_conf === "N") {
            return contacts;
        }
    }
}

// function to find a contact entry by name and return that entry's dictionary
function findContact(contacts) {
    let input_name = prompt("Enter the name of the contact you wish to find. ");
    let index_num;
    let found = "N";
    contacts.forEach(
        function(contact) {
            if (contact[name.toUpperCase()] === input_name.toUpperCase()) {
                let found = "Y";
                let input_name = contact[name];
                let fav_color = contact[favoriteColor];
                let fav_fruit = contact[favoriteFruit];
                if (found === "Y") {
                    let modify = prompt(`An entry was found for ${input_name} who loves ${fav_fruit} and the color ${fav_color}. Would you like to modify this entry('Y' or 'N')? `);
                    if (modify.toUpperCase === "Y") {
                        var contacts = edit_contact(contacts, index_num);
                    } else { 
                        break;
                    }
                } else if (found === "N") {
                    break;
                } 
            }
        }
    );
    
     {
        
    }
    return contact, index_num
} ;
// contact, index_num = find_contact(contacts)

function edit_contact(contacts, index_num) {
    let contact = contacts[index_num];
    let old_contact = contacts[index_num];
    let old_name = old_contact["name"];
    let old_color = old_contact["favorite color"];
    let old_fruit = old_contact["favorite fruit"];
    let input_name = contact["name"];
    let fav_color = contact["favorite color"];
    let fav_fruit = contact["favorite fruit"];
    while (true) {
        let change_opt = prompt("Entry found for {input_name} who loves {fav_fruit} and the color {fav_color}. Would you like to modify this entry? Enter 'Y' to edit, 'D' to delete, or 'N' to abort. ");
        if (change_opt.upper() === "Y") {
            let change_cat = prompt(`${input_name} loves ${fav_fruit} and the color ${fav_color}. Enter 'name', 'fruit' or 'color' to change a category, or 'cancel' to abort editing. `);
            if (change_cat.toUpperCase() === "CANCEL") {
                break;
            } else if (change_cat.toUppercase() === "NAME") {
                let new_name = prompt("Enter the new name for this entry. ");
                let name_conf = prompt(`Set the name to ${new_name}('Y' or 'N')? `);
                if (name_conf.toUppercase() === "Y") {
                    input_name = new_name;
                    continue;
                }
            } else if (change_cat.toUppercase() === "FRUIT") {
                let new_fruit = prompt("Enter the new favorite fruit for this entry. ");
                let fruit_conf = prompt(`Set favorite fruit to ${new_fruit}('Y' or 'N')? `);
                if (fruit_conf.toUppercase() === "Y") {
                    fav_fruit = new_fruit;
                    continue;
                }
            } else if (change_cat.toUppercase() === "COLOR") {
                    let new_color = prompt("Enter the new favorite color for this entry. ");
                    let color_conf = prompt(`Set favorite color to ${new_color}('Y' or 'N')? `);
                        if (color_conf.toUppercase() === "Y") {
                            fav_color = new_color;
                            continue;
                        } else {
                        break;
                        }
            }
            let change_conf = prompt(`This entry was for ${old_name} who loved ${old_fruit} and the color ${old_color}.\n Would you like to change this to show ${input_name} loves ${fav_fruit} and the color ${fav_color} ('Y' or 'N')? `);
            if (change_conf.toUppercase() === "Y") {
                contact["name"] = input_name
                contact["favorite fruit"] = fav_fruit
                contact["favorite color"] = fav_color
                contacts[index_num] = contact
                return contacts;
            } else {
                break;
            }
        } else if (change_opt.toUppercase() === "D") {
            contacts = delete_contact(contacts, index_num);
        } else {
            break;
        }
    }
}

function delete_contact(contacts, index_num) {
    contacts.splice(index_num, 1);
    return contacts;
}

while (true) {
    let main_choice = prompt("Welcome to the main menu of your contact list of people and their favorite color/fruit, for whatever reason.\nEnter 'find' to view or modify a contact, 'new' to enter a new contact, 'save' to save changes made, or 'quit' to quit.");
    if (main_choice.toUppercase() == "FIND") {
        contact, index_num = find_contact(contacts)
    } else if (main_choice.toUppercase() === "NEW") {
        contacts = create_contact(contacts);
    } else if (main_choice.toUppercase() === "QUIT") {
        break;
    }
}
