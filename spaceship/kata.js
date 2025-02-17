// Given an array of attack damages and a shield capacity for a spaceship, return the index when cumulative damage exceeds the shield. Return -1 if shield survives.
// > findShieldBreak([10, 20, 30, 40], 50)
// > 2

// > findShieldBreak([1, 2, 3, 4], 20)
// > -1

// > findShieldBreak([50], 30)
// > 0


function findShieldBreak(arr, capacity){
    let res = 0;
    let newArr = arr.slice();
    let amountAttack = 0

    for(let i=0; i < newArr.length; i ++){
        index = i;
        amountAttack += newArr[i];

        if(amountAttack > capacity){
            res = index;
            return res
        }
        else if(amountAttack < capacity && index == newArr.length - 1){
            res = - 1;
            return res
        }
        else if(amountAttack === capacity){
            res = index;
            return res;
        }
        else {
            continue;
        }   
    }  
    // si amountAttack n'a ajamais déppassé capacity:
    return res=  - 1; 
}

let result = findShieldBreak([1, 2, 3, 4], 20)
console.log("🍭 ", result)