

class Node:
    def __init__(self,newData):


        self.data = newData
        self.next = None





def traversal(head):

    while head is not None:
        print(head.data,end =" ")
        head = head.next

    return head


def insertionAtFront(head,newData):

    newHead = Node(newData)

    newHead.next = head

    return newHead


def insertionAtBack(head,newData):

    last = Node(newData)

    temp = head

    while temp.next is not None:
        temp = temp.next

    temp.next = last


    return head


def insertAtPosition(head, newData, position):

    if position < 1:
        return head

    newNode = Node(newData)

    if position == 1:
        newNode.next = head
        return newNode

    temp = head
    currentPosition = 1

    while temp is not None and currentPosition < position - 1:
        temp = temp.next
        currentPosition += 1

    if temp is None:
        return head

    newNode.next = temp.next
    temp.next = newNode

    return head


def deleteAtFront(head):

    if head is None:

        return head

    head = head.next

    return head


def deleteAtBack(head):


    if head is None:
        return None

    if head.next is None:
        return None

    secondLast = head

    while secondLast.next.next is not None:
        secondLast = secondLast.next

    secondLast.next = None


    return head


def deleteAtPosition(head,position):

    if head is None:
        return None

    if position == 1:
        
        return head.next

    currentPosition = 1
    
    temp = head

    while temp.next is not None and currentPosition < position -1:

        temp = temp.next

        currentPosition +=1

    
    temp.next = temp.next.next



    return head


def searchKey(head,key):

    if head is None:
        return False


    if head.data == key:
        return True

    
    return searchKey(head.next,key)


def reverseLinkedList(head):

    nodes = []
    temp = head

    if head is None:
        return head

    if head.next is None:
        return head

    while temp is not None:
        nodes.append(temp.data)
        temp = temp.next

    # here we can used two point as well
    nodes = nodes[::-1]

    temp = head
    for value in nodes:

        temp.data = value
        temp = temp.next

    return head


def modifyLinkedList(head):

    nodes = []
    temp = head

    if head is None:
        return head

    if head.next is None:
        return head

    while temp is not None:
        nodes.append(temp.data)
        temp = temp.next

    left = 0
    right = len(nodes) -1

    while left < right:

        values = nodes[left] - nodes[right]

        nodes[left],nodes[right] = values, nodes[left]

        left+=1
        right-=1

    temp = head
    for value in nodes:

        temp.data = value
        temp = temp.next

    return head








head = Node(20)

head.next = Node(30)

head.next.next = Node(40)





# traversal(head)

##### inisert new date ####

# head = insertionAtFront(head,10)

# head = insertionAtBack(head,50)

# head = insertAtPosition(head,100,5)

# head = deleteAtFront(head)

# head = deleteAtBack(head)

# head = deleteAtPosition(head,1)

# key1 = searchKey(head,20)

# key2 = searchKey(head,200)

# key3 = searchKey(head,40)

# print(key1,key2,key3)

#head = reverseLinkedList(head) 
head = modifyLinkedList(head)

traversal(head)







