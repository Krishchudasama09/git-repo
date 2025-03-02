class employees:
    a=1
    @classmethod
    def show(self):
        print(f"this a claas atribute  {self.a}")

e=employees()
e.a=100

e.show()