


def main():

 class student:

  def __init__(self, name, grade ):
      # _init_ is a special method in python called the constuctor method
      #self is not a parameter it just refers to the student
    self.name = name
    # Name is an attribute
    self.grade = grade
    # grade is an atttribute
    self.gpa = 0.0
    # gpa is an attribute
  def record(self):

      return "Student {} is a {} with a {}".format(self.name,self.grade,self.gpa)

 #Each student is an object

 student1 = student("Tim", "Freshman")
 student1.gpa = 4.0
 student2 = student("Mary", "Senior")
 student2.gpa = 3.7
 student3 = student("Lily", "Junior")
 student3.gpa = 3.67

 print(student1.name)
 print(student1.gpa)
 print(student2.record())
main()
