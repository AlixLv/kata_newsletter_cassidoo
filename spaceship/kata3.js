function findShieldBreak(arr, shield){
    for (let i= 0; i < arr.length; i++){
        shield -= arr[i];

        if (shield < 0){
            return i;
        }
        else if (shield > 0 && i==arr.length -1){
            return -1;
        }
    }
}

let res = findShieldBreak([50], 30); 
console.log(res)

