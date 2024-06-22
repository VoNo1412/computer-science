def dectecCycle(self, head):
    slow = fast = head;

    while fast and fast.next:
        slow = slow.next;
        fast = fast.next.next;

        if slow == fast:
            start = head;

            while slow != start:
                slow = slow.next;
                start = start.next;

            return start;

        return  None;