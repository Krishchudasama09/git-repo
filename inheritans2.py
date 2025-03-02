class student1:
    name="krish"
    roll_no="122323354656"

    def krish1(self):
        print(f"name of student {self.name} and roll number {self.roll_no}")

class student2(student1):
    branch="IT"

    def krish2(self):
        print(f"name of branch {self.branch} ") #and roll number{self.roll_no}")

class student3(student2):
    collage="GPR"

    def krish3(self):
        print(f"name of collage {self.collage} ")#and roll number{self.roll_no}")

s1=student1()
s2=student2()
s3=student3()

#print(s1.name,s1.roll_no,s2.branch,s3.collage)

s1.krish1()


s2.krish2()


s3.krish3()


