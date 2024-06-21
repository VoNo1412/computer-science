class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class MyLinkedList(object):
    def __init__(self):
        self.head = None;


    def get(self, index):
        if index < 0 or self.head is None: return;
        count = 0;
        current_node = self.head;

        while current_node:
            if count == index: return current_node.data;
            current_node = current_node.next;
            count += 1;

        return -1;


    def addAtHead(self, val):
        newNode = Node(val);
        newNode.next = self.head;
        self.head = newNode;

    def addAtTail(self, val):
        newNode = Node(val);
        if self.head is None: self.head = newNode; return;

        current_node = self.head;
        while current_node.next:
            current_node = current_node.next;

        current_node.next = newNode;
    
    def addAtIndex(self, index, val):
        count = 0;
        current_node = self.head;
        newNode = Node(val);

        if index < 0: return;
        if index == 0: 
            newNode.next = self.head;
            self.head = newNode;
            return;
    
        if current_node is None: current_node = newNode

        while current_node:
            if count + 1 == index:
                newNode.next = current_node.next;
                current_node.next = newNode;
                return;

            current_node = current_node.next;
            count += 1;
    
    def deleteAtIndex(self, index):
        if index < 0 or self.head is None: return;
        if index == 0: self.head = self.head.next; return;


        count = 0;
        current_node = self.head;
        
        while current_node:
            if count + 1 == index and current_node.next:
                current_node.next = current_node.next.next;
                return;

            current_node = current_node.next;
            count += 1;


    def showLinkedList(self):
        current_node = self.head;
        while current_node:
            print('This is item: ', current_node.data);
            current_node = current_node.next;

obj = MyLinkedList();

obj.addAtHead(1)
obj.addAtHead(2)
obj.addAtHead(3)

obj.addAtTail(4)
obj.addAtIndex(1, 4)
obj.addAtIndex(0, 9)

obj.deleteAtIndex(1)
obj.deleteAtIndex(0)
obj.showLinkedList()

