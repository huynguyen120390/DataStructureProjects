#include <iostream>
using namespace std;

class node{
    public:
        int data;
        node * next;
};

class SinglyLinkedList{
    private:
    node *head, *tail;
    int length;
    public:
    SinglyLinkedList(){
        head = NULL;
        tail = NULL;
        length = 0;
    }

    void append(int data){
        node *newNode = new node;
        (*newNode).data = data;
        (*newNode).next = NULL;

        if(head==NULL){
            head = newNode;
            tail = newNode;
        }else{
            (*tail).next = newNode;
            tail = newNode;
        }
        length ++;

    }

    void prepend(int data){
        node *newNode = new node;
        newNode->data = data;
        if(head==NULL){
            head = newNode;
            tail = newNode;
        }else{
            newNode->next = head;
            head = newNode;
        }
        length ++;
    }

    node * transverse_to_index(int index){
        node *curr = head;
        int count = 0;
        while(curr != NULL){
            if(count < index){
                curr = curr->next;
                count++;
            }else{
                break;
            }
        }
        return curr;
    }

    void eliminate(int index){
        if(head == NULL){
            throw "EmptyList";
        }else if (index < 0 || index >= length ) {
            throw "OutOfBound";
        }else if(index == 0 ){
            if(length == 1){
                head = NULL;
                tail = NULL;
            }else{
                node * curr = head;
                head = head->next;
                curr->next = NULL;
                curr = NULL;

            }
        }else{
            node *at= transverse_to_index(index);
            node *before = transverse_to_index(index - 1);
            if (index == length - 1){
                tail = before;
                before->next = NULL;
                at = NULL;
            }else{
                before->next = before->next->next;
                at->next=NULL;
                at=NULL;
            }
            
        }
        length--;
    }

    int lookup(int data){
        node * curr = head;
        int count = 0;
        while(curr!=NULL){
            if(data != curr->data){
                curr = curr->next;
                count++;
            }else{
                return count;
            }
        }
        return -1;
    }

    void display(){
        node *curr = head;
        cout<<"Length of "<< length <<endl;
        cout<<"head->";
        while(curr!=NULL){
            cout << curr->data << "->";
            curr = curr->next;
        }
        cout<<"NULL\n";
    }

};

int main(){
    SinglyLinkedList sll;
    sll.append(1);
    sll.append(2);
    sll.append(3);
    sll.append(4);
    sll.append(5);
    sll.append(6);
    sll.prepend(7);
    sll.prepend(8);
    sll.prepend(9);
    sll.prepend(10);
    sll.display();
    sll.eliminate(0);
    sll.eliminate(8);
    sll.eliminate(2);
    printf("Index %d\n",sll.lookup(9));
    sll.display();

    return 0;
}