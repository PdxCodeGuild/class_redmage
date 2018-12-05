let contactList = [{displayName:"Chad Bean", firstName:"Chad", lastName:"Bean", address:"120 South Grove St", city:"Missoula", state:"MT"},
                {displayName:"Jessica Bean", firstName:"Jessica", lastName:"Mao", address:"255 Bean Lane", city:"Missoula", state:"MT"},
                {displayName:"Robert Bean", firstName:"Robert", lastName:"Bean", address:"2520 Larkinwood Dr", city:"Missoula", state:"MT"}, 
                
                ]

let userText = document.getElementById("idinputSearchContacts")
let btnSearch = document.getElementById("idbtnSearch")
let changeContactbtn = document.getElementById("changeContact")

btnSearch.addEventListener("click", function() {
    searchText = userText.value;
    searchText = searchText.toLowerCase();
    for (var key in contactList) {
        str = (contactList[key]["displayName"]);
        str = str.toLowerCase();
        test = str.search(searchText);

        if (test === 0) {
            outputName.value = contactList[key]["displayName"];
            outputAddress.value = contactList[key]["address"];
            outputCity.value = contactList[key]["city"];
            outputState.value = contactList[key]["state"];
            break;
        }
        else if( test === -1) {
            outputName.value = "";
            outputAddress.value = "";
            outputCity.value = "";
            outputState.value = "";
        
        }
        }
changeContactbtn.addEventListener("click", function() {
    console.log(contactList[key])
    console.log(contactList[key]["displayName"])
    contactList[key]["displayName"] = outputName.value
    contactList[key]["address"] = outputAddress.value;
    contactList[key]["city"] = outputCity.value;
    contactList[key]["state"] = outputState.value

})
    }
)