/**
 * 
 * Queue: FIFO
    Enqueue: Add an element to the end of the queue
    Dequeue: Remove an element from the front of the queue
    IsEmpty: Check if the queue is empty
    IsFull: Check if the queue is full
    Peek: Get the value of the front of the queue without removing it

    There are four different types of queues:
        Simple Queue
        Circular Queue
        Priority Queue
        Double Ended Queue
 */


class Queue {
    constructor(front = -1, rear = -1, queue = []) {
        this.front = front;
        this.rear = rear;
        this.queue = queue;
        this.size = 3;
    }

    enqueue(element) {
        if(this.isFull()) {
           console.log("queue is full");
           return;
        }

        if(this.front === -1) this.front = 0;

        this.rear += 1;
        this.queue[this.rear] = element;
    }

    dequeue() {
        if(this.isEmpty()) {
            console.log("queue is empty");
            return;
        }

        let element = this.queue[this.front];
        delete this.queue[this.front];

        if(this.front >= this.rear) {
            this.front = -1;
            this.rear = -1;
            return;
        }
        this.front += 1;

        return element;
    }

    isFull() {
        if(this.front === 0 && this.rear === this.size - 1) {
            return true;
        }

        return false;
    }

    isEmpty() {
        if(this.front === -1) {
            return true;
        } 

        return false;
    }

    show() {
        console.log("queue: ", this.queue);
    }
}

const initQueue = new Queue();

initQueue.enqueue(4);
initQueue.enqueue(1);
initQueue.enqueue(2);
initQueue.enqueue(2);

initQueue.show();

console.log("dequeue: ", initQueue.dequeue())

 
