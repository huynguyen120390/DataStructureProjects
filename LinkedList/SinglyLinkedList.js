/**
 * Autho
 * Implement Singly Linked List in JS 
 * functions of show_as_list, append, prepend, insert, delete
*/

class SinglyLinkedListNode{
    constructor(value){
        this.value = value;
        this.next = null;
    }

}
class SinglyLinkedList{
    //Create a head pointing to pair of {value, next}
    //Point tail to head
    constructor(value){
        this.head = {
            value: value,
            next: null
        }
        this.tail = this.head;
        this.length = 1;
    }

    /**
     * Append a node at the end of the linked list
     * @param {int/float} value  int/float value 
     * @return {SinglyLinkedList} this 
     */
    append(value){
        const newNode = new SinglyLinkedListNode(value);
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this;
    }

    /**
     * Prepend a node at the begining of the linked list
     * @param {int/float} value  int/float value
     * @return {SinglyLinkedList} this 
     */
    prepend(value){
        const newNode = new SinglyLinkedListNode(value);
        newNode.next = this.head;
        this.head = newNode;
        this.length++;
        return this;
    }

    traverse_to_index(index){
        let curr = this.head;
        let counter = 0;
        if(index < 0 || index >= this.length){
            throw "OutBoundOfLinkedList";

        }else{
            while(counter < index){
                counter++;
                curr = curr.next;
            }
        }
        return curr;
    }

    /**
     * Insert a node at a position on the linked list
     * @param {int} index           Position 
     * @param {int/float} value  Value
     * @return {SinglyLinkedList} this
     */
    insert(index,value){
        const newNode = new SinglyLinkedListNode(value);

        if(index == 0){
            this.prepend(value);
        }else if(index == this.length){
            this.append(value);
        }else if((index > this.length) || (index < 0 )){
            throw "OutBoundOfLinkedList";
        }else{
            let curr = this.traverse_to_index(index - 1);
            newNode.next = curr.next;
            curr.next = newNode;
            this.length ++;
        }
        return this;
    }

    /**
     * Delete a node at a position on the linked list
     * @param {int} index
     * 
     */
    delete(index,value){
        const newNode = new SinglyLinkedListNode(value);
        if(index < 0 || index >= this.length){
            throw "OutBoundOfLinkedList";
        }else if (index == 0){
            this.head = this.head.next;
        } else{
            let curr_before = this.traverse_to_index(index - 1);
            let curr_at = this.traverse_to_index(index);
            curr_before.next = curr_before.next.next;
            curr_at.next = null;
        }
        this.length--;
    }

    /**
     * Show linked list as in form of a list, for debug purposes
     * @param none 
     * @return void
     */
    show_as_list(){
        const arr = [];
        console.log("Length " + this.length);
        if(this.length == 0){
            arr.push(null);
        }else{
            let curr = this.head;
            while(curr !== null){
                arr.push(curr.value);
                curr = curr.next;
            }            

        }
        return arr;
    }



}

const sll = new SinglyLinkedList(10);
sll.append(1);
sll.append(2);
sll.append(3);
sll.insert(3,6);
sll.insert(5,8);
console.log(sll.show_as_list());
sll.delete(1);
console.log(sll.show_as_list());

