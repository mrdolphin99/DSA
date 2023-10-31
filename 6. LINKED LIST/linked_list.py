class Node:
    def __init__(self, value):#-------> O(1) / O(1)
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self):#-------> O(1) / O(1)
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):# APPEND AN ELEMENT INTO SLL
        new_Node = Node(value) 
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        self.length +=1
    
    def prend(self, value):# PREND AN ELEMENT INTO SLL
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def insert(self,index,value): #Insert an element into sll
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0 :
            self.head = new_node
            self.tail = new_node
        if index == 0:
            new_node.next = self.head 
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index -1):
                temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length +=1
        return True
    
    def traverse(self):
        current = self.head
        while current: #is not none
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head 
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index +=1
        return -1
    
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next 
        return current
    
    def set_value(self, index, any_value):
        temp = self.get(index)
        if temp:
            temp.value = any_value
            return True
        return False
    
    def pop_first(self): #pop and return the popped node
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -=1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp 
            temp.next = None
        self.length -=1
        return popped_node
    
    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1 or index == -1:
            return self.pop()
        prev_node = self.get(index -1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node = None
        self.length -=1
        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next#Saves the next node before overwriting current_node.next in the next step.
            current_node.next = prev_node#Reverses the link by setting the next of current_node to prev_node.
            prev_node = current_node#Updates prev_node to current_node for the next iteration.
            current_node = next_node#Moves the current_node one step forward for the next iteration.
        self.head, self.tail = self.tail, self.head# After the end of the loop, the head and tail are swapped to complete the reversal of the linked list

    def finding_middle(self): #using fast and slow method
        if not self.head:
            return None
        slow = self.head
        fast = self.head 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def remove_duplicates(self):
        if self.head is None:
            return 'SLL has no value!'
        node_values = set()
        current_node = self.head
        node_values.add(current_node.value)
        while  current_node.next:
            if current_node.next.value in node_values:
                current_node.next = current_node.next.next
                self.length -=1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node
    
    def merge_twoSorted_SLL(self, l1, l2):
        preHead = LinkedList(-1)
        prev = preHead
        while l1 and l2:
            if l1.value <= l2.value:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2 
                l2 = l2.next
            prev = prev.next
    
        prev.next = l1 if l1 is not None else l2
        return preHead.next
    
    def delete_duplicate(self, head):
        current = head 
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
    def removeElements(self, head, target):
        dummy_head = LinkedList(-1)
        dummy_head.next = head
        prev_node = dummy_head
        current_node = head
        while current_node:
            if current_node.val == target:
                prev_node.next == current_node.next
            else:
                prev_node = current_node
            current_node = current_node.next
        return dummy_head.next

    def __str__(self):
        temp_Node = self.head 
        result = ''
        while temp_Node is not None:
            result += str(temp_Node.value)
            if temp_Node.next is not None:
                result +="->"
            temp_Node = temp_Node.next
        return result

new_linked_list = LinkedList()
new_linked_list.append(10) # APPEND AN ELEMENT INTO EMPTY SLL
new_linked_list.append(20)
new_linked_list.append(30)
#print(new_linked_list)                     
new_linked_list.prend(40)
print(new_linked_list)  
new_linked_list.insert(3,50)
new_linked_list.traverse()
print(new_linked_list.search(50))
#print(new_linked_list.get(2))
print(new_linked_list.set_value(2,60))
print(new_linked_list)
print(new_linked_list.pop_first())
print(new_linked_list)
print(new_linked_list.pop())
print(new_linked_list)