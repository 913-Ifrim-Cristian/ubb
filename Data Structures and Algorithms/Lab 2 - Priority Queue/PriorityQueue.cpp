
#include "PriorityQueue.h"
#include <exception>
#include <iostream>
using namespace std;


PriorityQueue::PriorityQueue(Relation r) {
    /*
     * Theta(1)
     */

    this->rel = r;
    this->head = nullptr;
    this->tail = nullptr;
}


void PriorityQueue::push(TElem e, TPriority p) {
    /*
     * Best case: Theta(1) -> If head is NULL, if the priority of e is better than the head, or being last elem
     * Worst case: Theta(n), where n = the number of elements in the queue -> The element is added before the end.
     * Average case: Theta(n)
     * Total complexity: O(n)
     */
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
        while(!this->rel(p, h->val.second)) {
            h = h->next;
        }

        node *ptr = new node;
        ptr->val = Element(e, p);

        ptr->next = h;
        ptr->prev = h->prev;

        h->prev->next = ptr;
        h->prev = ptr;
    }
}

//throws exception if the queue is empty
Element PriorityQueue::top() const {
    /*
     * Theta(1)
     */
	//TODO - Implementation
    if(this->isEmpty())
        throw exception();

	return this->head->val;
}

Element PriorityQueue::pop() {
    /*
     * Theta(1)
     */

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
	/*
	 * Theta(1)
	 */
	return this->head == nullptr;
}


PriorityQueue::~PriorityQueue() {
    /*
     * Theta(n), where n = the number of elements in the queue
     */
	while(this->head != nullptr) {
        node* aux = this->head;
        this->head = this->head->next;
        delete aux;
    }
}

void PriorityQueue::merge(PriorityQueue &pq) {
    /*
     * Best case: Theta(n), where n = the number of elements in pq, all elems added at the start or the end
     * Worst case: Theta(n*m), where n = the number of elements in pq, m = no of elems in this queue, all elems added before the end of the queue
     * Average case: Theta(n*m)
     * Total complexity: O(n*m)
     */

    while(!pq.isEmpty()) {
        Element e = pq.pop();
        this->push(e.first, e.second);
    }
}

