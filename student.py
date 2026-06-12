class Student:
    def __init__(self, name, student_id, marks, age):
        self.__name = name
        self.__student_id = student_id
        self.__marks = marks
        self.__age = age

    def get__marks(self):
        return self.__marks

    def set__marks(self, new_marks):
        if isinstance(new_marks, (int, float)):  # ✅ correct type check
            self.__marks = new_marks
        else:
            print("Invalid data")

    def validate_marks(self):
        # ✅ Guard against non-numeric marks like "hehe"
        if not isinstance(self.__marks, (int, float)):
            return False
        return 0 <= self.__marks <= 100

    def validate_age(self):
        # ✅ Guard against non-numeric age
        if not isinstance(self.__age, (int, float)):
            return False
        return self.__age > 20

    def check_qualification(self):
        # ✅ Check validity first, then qualification threshold
        if not self.validate_marks() or not self.validate_age():
            print(f"{self.__name}: Invalid data")
        elif self.__marks >= 65:
            print(f"{self.__name}: Qualified")
        else:
            print(f"{self.__name}: Not qualified")


S1 = Student("Shikha", 101, 70, 20)
S1.check_qualification()   # age=20, not > 20 → Not qualified

S2 = Student("Suniti", 102, 80, 21)
S2.check_qualification()   # age=21, marks=80 ✅ → Qualified

S3 = Student("Tanish", 103, "hehe", 20)
S3.check_qualification()   # marks="hehe" → Invalid data