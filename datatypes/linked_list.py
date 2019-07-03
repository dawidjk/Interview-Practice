class Node:
  def __init__(self, data=None, key=None):
    self.data = data
    self.key = key
    self.next = None
    self.previous = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_node(self, data, key=None):
    temp = Node(data, key)
    if self.head is None:
      self.head = temp
      self.tail = temp
    else:
      temp.previous = self.tail
      self.tail.next = temp
      self.tail = self.tail.next

  def first(self):
    return self.head

  def last(self):
    return self.tail

  def find(self, data):
    temp = self.head

    while temp is not None:
      if temp.data == data:
        return temp
      temp = temp.next

  def find_key(self, key):
    temp = self.head

    while temp is not None:
      if temp.key == key:
        return temp
      temp = temp.next

