var Console = function () {
    this.log = function(msg){ debug(msg) }; 
};
var console = new Console();

function find_number_with_firstRecurrent(arr){
    let logTable = {};
    let num = null;
    for(let i = 0; i < arr.length ; i++){
        logTable[arr[i]] = null;
    }

    for(let i = 0; i < arr.length ; i++){
        if(logTable[arr[i]] == null){
            logTable[arr[i]] = 1;
        }
        else if (logTable[arr[i]] == 1){
            num = arr[i];  
            break;
        }  
    }
    return num;
}

var arr = [2,5,1,2,3,5,1,2,4];
var arr2 = [2,1,1,2,3,5,1,2,4];
var arr3 = [2,3,4,5];
var arr4 = [];
var arr5 = null;

var num = find_number_with_firstRecurrent(arr);
console.log(num);