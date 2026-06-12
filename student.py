#Statement: A university wants to automate their admission process. Students are admitted based on the marks scored in the qualifying exam. A student is identified by student id, age and marks in qualifying exam. Data are valid, if:

#Age is greater than 20
#Marks is between 0 and 100 (both inclusive)
#A student qualifies for admission, if

#age and marks are valid and
#Marks is 65 or more
#Write a python program to represent the students seeking admission in the university. The details of student class are given below.


class Student:
    def __init__(self, name,student_id, marks, age):
        self.__name = name
        self.__student_id = student_id
        self.__marks = marks
        self.__age = age

    def get__marks(self):
        return self.__marks
    def set__marks(self,new_marks):
        if new_marks == int:
            return new_marks
        else :
            return "invalid data "


    def validate_marks(self):
        return 0 <= self.__marks <= 100
        
    def validate_age(self):
       return self.__age > 20

    def check_qualification(self):
        if self.validate_age() and self.validate_marks() and self.__marks >= 65:
            print("qualified")
        else:
            print("not qualified")


S1 = Student("shikha",101,70,20)
S1.check_qualification()

S2 = Student("suniti",102,80,21)
S2.check_qualification()

S3 = Student("tanish",103,"hehe",20)
S3.check_qualification()




        
