/**
 * 
 * Stack is LIFO
 *  Push: Add an element to the top of a stack
    Pop: Remove an element from the top of a stack
    IsEmpty: Check if the stack is empty
    IsFull: Check if the stack is full
    Peek: Get the value of the top element without removing it
 */

class StackQueue {
  constructor(stack = [], size = 10) {
    this.stack = stack;
    this.size = size;
  }

  push(element) {
    return this.isFull() ? "Stack is full!" : this.stack.push(element);
  }
  pop(element) {
    return this.isEmpty
      ? "Cannot remove element because stack is empty!"
      : this.stack.pop(element);
  }
  isEmpty() {
    return !this.stack.length ? true : false;
  }
  isFull() {
    return this.stack.length == this.size ? true : false;
  }
  Peek() {}
}

const initStack = new StackQueue();
initStack.push(4);
console.log("stack_push: ", initStack);

initStack.pop(1);
console.log("stack_pop: ", initStack);

initStack.push(2)
console.log("check empty: ", initStack.isEmpty());  
