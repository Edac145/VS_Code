class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        newNode = Node(data,self.head)
        self.head = newNode

    def print(self):
        if self.head is None:
            print("Linked List is Empty.")
            return
        
        itr=self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count
    
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
            return
        
        if index == 0:
            self.head =self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                newNode = Node(data,itr.next)
                itr.next = newNode

            itr = itr.next
            count += 1
    
    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return
        
        count = 0
        itr=self.head

        while itr:
            if itr.data == data_after:
                self.insert_at(count+1,data_to_insert)
            
            count += 1
            itr = itr.next

    def remove_by_value(self,data):
        if self.head is None:
            return
        
        count = 0
        itr=self.head

        while itr:
            if itr.data == data:
                self.remove_at(count)

            count += 1
            itr = itr.next



if __name__ == '__main__':
    ll=linkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_after_value("mango","apple")
    ll.insert_after_value("banana","figs")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    