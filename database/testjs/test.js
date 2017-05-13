console.log("sup");

// AKQJT98765432
// hdcs
var card_re = new RegExp('[AKQJT98765432][hdcs]', 'i');

function checkFlop(input) {
    var match = card_re.exec(input);
    if (match) {
        console.log(match);
    }
    else {
        console.log("nahhhhhhh")
    }
}