/**
 * @param {number} n
 * @return {number}
 */
var pivotInteger = function(n) {
    let pivot = Math.sqrt(n * (n + 1) / 2);
    if(Number.isInteger(pivot)){
        return Math.floor(pivot);
    }else{
        return -1;
    }
};

