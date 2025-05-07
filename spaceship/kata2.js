// Given an array of attack damages and a shield capacity for a spaceship, 
// return the index when cumulative damage exceeds the shield. Return -1 if shield survives.

// > findShieldBreak([10, 20, 30, 40], 50)
// > 2

// > findShieldBreak([1, 2, 3, 4], 20)
// > -1

// > findShieldBreak([50], 30)
// > 0


function findShieldBreak(arr, capacity){
    let res = 0;
    let newArr = arr.slice();
    console.log("newArr: ", newArr);
    let amountAttack = 0;
    let i = 0;

   while(i < arr.length){
        console.log("🥟 valeur: ", arr[i], " index: ", i);
        amountAttack += arr[i];
        console.log("🍘 total: ", amountAttack);

        if(amountAttack > capacity){
            res = i;
            console.log("résultat dans if: ", res);
            return res;
        }
        else if(amountAttack < capacity && i == arr.length - 1){
            res = -1;
            console.log("résultat dans else if: ", res);
            return res;
        }
        else if(amountAttack === capacity){
            res = i;
            return res;
        }
        else{
            i++;
            continue; 
        }
    }  

    return res = -1;

}

let result = findShieldBreak([10, 20, 30, 40], 50)
console.log("🍭 ", result)