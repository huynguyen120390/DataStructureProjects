#include <stdio.h>

struct node{
    int data;
    struct node * next;
};

int length(struct node * head){
    struct node * curr = head;
    int length = 0;
    while(curr!=NULL){
        length++;
    }
    return length;
}

struct node * traverse(struct node * head, int index){
    if(head == NULL){

    }else{
        struct node * cur = head;
        int count = 0;
        while(count < index){
            count++;
            cur = cur->next;
        }
    }
}





