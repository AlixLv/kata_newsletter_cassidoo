// Given two strings, s and p, return an array of all the start indices of p's anagrams in s.

// Examples:
// findAnagrams("cbaebabacd", "abc")
// > [0, 6]

// findAnagrams("fish", "cake")
// > []

// findAnagrams("abab", "ab")
// > [0, 1, 2]

function compareLst(initalLst, subLst){
    let checkStr = "";
    let res;
    for(let i = 0; i < subLst.length; i++){
        if(initalLst.includes(subLst[i]) && checkStr.includes(subLst[i]) === false){
            checkStr += subLst[i];
            res = true;
        }
        else{
            return res = false;
        }
    }

    return res;
}


function findAnagrams(strS, strP){
    let myList = [];
    let maxLength = strP.length;

    for(let i = 0; i < strS.length; i++){
        let currentIndex = i;
        let currentPart = i + maxLength
        let subStr = "";

        for(let j = i; j < currentPart; j++){
            subStr += strS[j];

            if(currentPart > strS.length){
                return myList;
            }
            else{
                continue;
            }
        }
        console.log("subStr après for loop: ", subStr, typeof(subStr));
        let res = compareLst(strP, subStr);

        res === true ? myList.push(currentIndex) : console.log("false") ;
 
    }

    return myList;
}


let result = findAnagrams("fish", "cake")
console.log("result: ", result)