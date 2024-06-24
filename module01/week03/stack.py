#Exercise 3:

class MyStack:
  def __init__(self, capacity):
    self.__capacity = capacity
    self.__stack = []
  
  def get_stack(self):
    return self.__stack
  
  def is_empty(self):
    return len(self.__stack) == 0

  def is_full(self):
    return len(self.__stack) == self.__capacity

  def push(self, element):
    if self.is_full():
      return "Overflow"
    return self.__stack.append(element)
  
  def pop(self):
    if self.is_empty():
      return "Underflow"
    return self.__stack.pop()
  
  def top(self):
    if self.is_empty():
      return "Underflow"
    return self.__stack[-1]
