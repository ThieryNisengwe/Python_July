/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";


function no_double(str){
    var x = new Set();
    for(var i=0; i<str.length; i++)
    x.add(str[i]);
    console.log(x)
    console.log(i)
    let string = ''
    for (const v of x){
        string += v
    }
    return string
}

console.log(no_double('lolipops'))








// //bonus
// const str5 = "aba"
// const expected5 = "ba"

// /**
//  * De-dupes the given string.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str A string that may contain duplicates.
//  * @returns {string} The given string with any duplicate characters removed.
//  */
// // function no_double(str) {
//     //Your code here
// // }

console.log(no_double(str1));
console.log(no_double(str2));
console.log(no_double(str3));
console.log(no_double(str4));
// console.log(no_double(str5));

/*****************************************************************************/

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

// const strA = "hello";
// const expectedA = "olleh";

// const strB = "hello world";
// const expectedB = "olleh dlrow";

// const strC = "abc def ghi";
// const expectedC = "cba fed ihg";

// /**
//  * Reverses the letters in each words in the given space separated
//  * string of words. Does NOT reverse the order of the words themselves.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str Contains space separated words.
//  * @returns {string} The given string with each word's letters reversed.
//  */
// function reverseWords(str) {
//     //Your code here
// }

// console.log(reverseWords(strA)) //expectedA: olleh
// console.log(reverseWords(strB)) //expectedB: olleh dlrow
// console.log(reverseWords(strC)) //expectedC: cba fed ihg