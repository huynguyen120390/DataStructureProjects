var Console = function () {
    this.log = function(msg){ debug(msg) }; 
};
var console = new Console();

console.log("hello");

class HashTable{
    constructor(size){
        this.data = new Array(size);
        this.size = size;
    }

    _hash(key){
        let hash = 0;
        for (let i = 0; i < key.length; i++){
            hash = (hash + key.charCodeAt(i) * i) % this.size;
        }
        return hash;
    }

    set(key, value){
        let hash = this._hash(key);
        if( !this.data[hash]){
            this.data[hash] = []; //if empty, create a new band of buckets
        }
        this.data[hash].push([key,value]); //add pair of key/value to bucket
    }

    get(key){
        let hash = this._hash(key);
        if(!this.data[hash]){
            return null;
        }
        else{
            let currentBucket = this.data[hash];
            for(let i = 0; i < currentBucket.length; i++){
                if (currentBucket[i][0] == key){
                    return currentBucket[i][1];
                }
            }
        }
        return null;
    }

    keys(){
        const keysArr = []
        for(let i = 0; i < this.data.length; i++){
            if(this.data[i]){
                for(let j = 0; j < this.data[i].length; j++){
                    keysArr.push(this.data[i][j][0]);
                }
            }
        }
        return keysArr;

    }
}

const myHashTable = new HashTable(3);
myHashTable.set("Grape","Big");
myHashTable.set("Flower","Big");
myHashTable.set("Grape2","Big");
myHashTable.set("Flowe2r","Big");
myHashTable.set("Grape23","Big");
myHashTable.set("Flowe2r","Big");
myHashTable.set("Flowe2r","Big");
console.log(myHashTable.keys());


