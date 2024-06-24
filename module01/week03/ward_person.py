#Exercise 2:

from abc import ABC, abstractmethod

class Person(ABC):
  def __init__(self, name, yob):
    self._name = name
    self._yob = yob

  @abstractmethod
  def describe(self):
    pass
  
  def get_yob(self):
    return self._yob

class Student(Person):
  def __init__(self, name, yob, grade):
     super().__init__(name, yob)
     self.__grade = grade

  def describe(self):
    print(f"Student - Name: {self._name}, YOB: {self._yob}, Grade: {self.__grade}")

class Teacher(Person):
  def __init__(self, name, yob, subject):
    super().__init__(name, yob)
    self.__subject = subject
  
  def describe(self):
    print(f"Teacher - Name: {self._name}, YOB: {self._yob}, Subject: {self.__subject}")

class Doctor(Person):
  def __init__(self, name, yob, specialist):
    super().__init__(name, yob)
    self.__specialist = specialist
  
  def describe(self):
    print(f"Doctor - Name: {self._name}, YOB: {self._yob}, Specialist: {self.__specialist}")

class Ward:
  def __init__(self, name:str):
    self.__name = name
    self.__list_people = list()
  
  def add_person(self, person:Person):
    self.__list_people.append(person)

  def describe(self):
    print(f"Ward Name: {self.__name}")
    for person in self.__list_people:
      person.describe()

  def count_doctor(self):
    count = 0
    for person in self.__list_people:
      if isinstance(person, Doctor):
        count += 1
    return count

  def sort_age(self):
    return self.__list_people.sort(key=lambda x: x.get_yob())

  def compute_average(self):
    count_teacher = 0
    total_age_teacher = 0
    for person in self.__list_people:
      if isinstance(person, Teacher):
        count_teacher += 1
        total_age_teacher += person.get_yob()
    return total_age_teacher / count_teacher


#test (a)
student1 = Student(name = 'Luan', yob = 2000, grade = "10")
student1.describe()

teacher1 = Teacher(name = 'Thai', yob = 1999, subject = "Math")
teacher1.describe()
techer2 = Teacher(name = 'Khanh', yob = 1998, subject = "progamming")
techer2.describe()

doctor1 = Doctor(name = 'Vinh', yob = 1984, specialist = "Computer science")
doctor1.describe()
doctor2 = Doctor(name = 'Phuc', yob = 1985, specialist = "Computer science")
doctor2.describe()

#test (b)
ward1 = Ward(name = "Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(techer2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

#test (c)
ward1.count_doctor()
#test (d)
ward1.sort_age()
ward1.describe()

#test (e)
ward1.compute_average()
