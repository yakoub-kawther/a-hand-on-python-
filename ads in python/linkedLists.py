class Node():
  def __init__(self , data):
    self.data=data
    self.next=None

class Linkedlist():
  def __init__(self):
     self.head=None


  def printlinkedlist(self):
    current = self.head
    while current:
      print(current.data , " ")
      current = current.next


  def insertingDataInBiginnig(self , data):
    if self.head==None:
       newnode=Node(data)
       self.head=newnode
    else:
      newnode=Node(data)
      newnode.next=self.head
      self.head=newnode
  
  def insertingDataInEnd(self,data):
    newnode=Node(data)
    prevNode=self.head
    if prevNode==None:
      self.head=newnode
    else:
      
      while prevNode.next !=None:
        prevNode=prevNode.next
      
    prevNode.next =newnode

  def insertBetween(self,previous , data):
    if previous is None :
       return
    else :
      newNode=Node(data)
      newNode.next=previous.next
      previous.next=newNode
  
  def deleatNode(self  , key):
    temp=self.head
    if temp is not None:
      if temp.data==key:
        self.head=temp.next
        temp=None
      else:
       while temp.next != None:
        if temp.data == key :
          break
        prev = temp
        temp = temp.next
      
       if temp==None:
        return
       else:
        prev.next=temp.next
        return
  
  def deleatHead(self):
    """
    temp=self.head
    if temp is not None : 
     self.head=temp.next
     temp=None
    """
    self.head=self.head.next


l=Linkedlist()
l.insertingDataInBiginnig(7)
l.insertingDataInBiginnig(10)
l.insertingDataInEnd(21)
l.insertingDataInEnd(25)
l.insertBetween(l.head,70)
l.printlinkedlist()
print()
l.deleatHead()
l.deleatNode(7)
l.printlinkedlist()
