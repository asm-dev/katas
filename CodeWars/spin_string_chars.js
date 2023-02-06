// Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed.
// Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

function spinWords(string) {
    let newStr = ""
    string.split(" ").forEach(word => {
        word.length < 5 ? newStr = newStr.concat(" ", word) : newStr = newStr.concat(" ", word.split("").reverse().join(""))    
    })
    return newStr.slice(1)
}

// Alternative and cleaner solution

// function spinWords(words){
//     return words.split(' ').map(word => {
//       return word.length >= 5 ? word : word.split('').reverse().join('');
//     }).join(' ');
// }
