
#include "PriorityQueue.h"
#include <exception>
#include <iostream>
using namespace std;


PriorityQueue::PriorityQueue(Relation r) {
	//TODO - Implementation
    this->rel = r;
    this->head = nullptr;
    this->tail = nullptr;
}


void PriorityQueue::push(TElem e, TPriority p) {
    //TODO - Implementation
    if (this->head == nullptr) {
        node *ptr = new node;

        ptr->val = Element(e, p);
        ptr->prev = nullptr;
        ptr->next = nullptr;

        this->head = ptr;
        this->tail = ptr;

        return;
    }

    if (this->rel(p, this->head->val.second)) {
        node *ptr = new node;

        ptr->val = Element(e, p);
        ptr->next = this->head;

        this->head->prev = ptr;
        ptr->prev = nullptr;

        this->head = ptr;

    } else if (!this->rel(p, this->tail->val.second)) {
        node *ptr = new node;

        ptr->val = Element(e, p);
        ptr->next = nullptr;

        ptr->prev = this->tail;
        this->tail->next = ptr;

        this->tail = ptr;

    }
    else {
        node* h = this->head;
        while(!this->rel(p, h->val.second))
            h = h->next;

        node* ptr = new node;
        ptr->val = Element(e, p);

        ptr->next = h;
        ptr->prev = h->prev;

        h->prev->next = ptr;
        h->prev = ptr;


    }
}

//throws exception if the queue is empty
Element PriorityQueue::top() const {
	//TODO - Implementation
    if(this->isEmpty())
        throw exception();

	return this->head->val;
}

Element PriorityQueue::pop() {
	//TODO - Implementation
    Element e = this->top();
    node* aux = this->head;
    if(this->head->next != nullptr)
        this->head = this->head->next;

    this->head->prev = nullptr;
    if(aux == this->tail) {
        this->head = nullptr;
        this->tail = nullptr;
    }

    delete aux;
	return e;
}

bool PriorityQueue::isEmpty() const {
	//TODO - Implementation
	return this->head == nullptr;
}


PriorityQueue::~PriorityQueue() {
	while(this->head != nullptr) {
        node* aux = this->head;
        this->head = this->head->next;
        delete aux;
    }
};

