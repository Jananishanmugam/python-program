class Node:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self,A):
        new_node = Node(A)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insertAtEnd(self,A):
        new_node = Node(A)
        if self.head is None:
            self.head = new_node
        else:
            invalue = self.head
            while invalue.next != None:
                invalue = invalue.next
            invalue.next = new_node
    
    def reversal(self):
        head = self.head
        ppt = self.head.next
        pt = self.head
        pt.next = None
        while ppt.next != None:
            head = ppt
            ppt = ppt.next
            head.next = pt
            pt = head
        head = ppt
        head.next = pt
        self.head = head
    
    def printList(self):
        head = self.head
        while head != None:
            print(head.val,end = " ")
            head = head.next
            
    def solve(self, B, C):
        new_node = Node(B)
        if C == 0:
            new_node.next = self.head
        else:
            pre_pointer = None
            pointer = self.head
            for i in range(C):
                pre_pointer = pointer
                if pointer.next != None:
                    pointer = pointer.next
            if pointer.next == None:
                pre_pointer.next = new_node
            else:
                pre_pointer.next = new_node
                new_node.next = pointer
                

s1 = Solution()
s1.insertAtEnd(1)
s1.insertAtEnd(2)
s1.insertAtEnd(3)
s1.printList()
print()
s1.reversal()
s1.printList()
# s1.solve(4,4)
# s1.printList()


# s2 = Solution()
# s2.insertAtBegin(1)
# s2.insertAtBegin(2)
# s2.insertAtBegin(3)
# s2.printList()
