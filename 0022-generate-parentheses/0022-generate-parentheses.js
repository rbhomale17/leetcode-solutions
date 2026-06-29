/**
 * @param {number} n
 * @return {string[]}
 */
 let arr = [];
var generateParenthesis = function(n) {
    arr = [];
     GenPar("",0,0,n);
     console.log(arr);
     return arr;
};


function GenPar(str = "",open = 0, close = 0,n){
    if(str.length==n*2){
        arr.push(str);
        return;
    }
    if(open<n){
        GenPar(str+'(',open+1,close,n);
    }
    if(open>close){
        GenPar(str+')',open,close+1,n);
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna