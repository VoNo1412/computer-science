class Node:
    # Create a Node
    def __init__(self, data):
        self.data = data;
        self.next = None;

class Linked_List:

    # Create a head
    def __init__(self):
        self.head = None;


if __name__ == "__main__":
    # create instance class 
    linkedList = Linked_List();


    # create instance class node
    linkedList.head = Node(1);
    second = Node(2);
    third = Node(3);

    # assigns connects node
    linkedList.head.next = second;
    second.next = third

    while linkedList.head != None:
        print("Note: ", linkedList.head.data)
        linkedList.head = linkedList.head.next


    