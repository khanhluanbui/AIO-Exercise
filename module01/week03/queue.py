# Exercise 4

class MyQueue:
  def __init__(self, capacity):
    self.__capacity = capacity
    self.__queue = []
  
  def get_queue(self):
    return self.__queue

  def is_empty(self):
    return len(self.__queue) == 0

  def is_full(self):
    return len(self.__queue) == self.__capacity
  
  def dequeue(self):
    if self.is_empty():
      return "Underflow"
    return self.__queue.pop(0)

  def enqueue(self, element):
    if self.is_full():
      return "Overflow"
    return self.__queue.append(element)

  def front(self):
    if self.is_empty():
      return "Underflow"
    return self.__queue[0]