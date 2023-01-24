
function alphabetPosition(text){
    const alphabetArr = [..."abcdefghijklmnopqrstuvwxyz"]
    let positionsArr = [];
    let textArr = text.toLowerCase().split("")
    textArr.forEach(char => {
        alphabetArr.includes(char) ? positionsArr.push(alphabetArr.indexOf(char)+1) : null 
    });
    return positionsArr.join(" ")
}

//alphabetPosition("The sunset sets at twelve o' clock.")
//"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"