let contactList = [{displayName:"Chad Bean", firstName:"Chad", lastName:"Bean", address:"120 South Grove St", city:"Missoula", state:"MT"},
                {displayName:"Jessica Bean", firstName:"Jessica", lastName:"Mao", address:"120 South Grove St", city:"Missoula", state:"MT"},
                {displayName:"Robert Bean", firstName:"Robert", lastName:"Bean", address:"120 South Grove St", city:"Missoula", state:"MT"}, 
                
                ]

let userText = document.getElementById("idinputSearchContacts")
let btnSearch = document.getElementById("idbtnSearch")

btnSearch.addEventListener("click", function() {
    searchText = userText.value;
    searchText = searchText.toLowerCase();
    for (var key in contactList) {
        str = (contactList[key]["displayName"]);
        str = str.toLowerCase();
        test = str.search(searchText);
        if (test == 0) {
            outputName.value = key["displayname"] 
        }
        }
    }
)