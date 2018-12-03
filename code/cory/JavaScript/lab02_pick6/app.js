winningTicket = [];
newTicket = [];
cashEarned = 0;


function generateTicket(list_name) {
    for (let i=0; i<5; ++i) {
        list_name.push(Math.ceil(Math.random() * 98));
    }
}

function compareTicket(new_ticket) {

    for (let i=0; i<winningTicket.length; ++i) {
        if (newTicket[i] === winningTicket[i]) {
            cashEarned +=2;
        }
    }

    newTicket = [];

}

generateTicket(winningTicket);

for (var numOfTickets=0; numOfTickets<1000; ++numOfTickets) {

    generateTicket(newTicket);
    compareTicket(newTicket);

}

alert(`You bought ${numOfTickets} tickets, and won a total of ${cashEarned} dollars.`)