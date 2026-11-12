# 파이썬 기초 11: 클래스와 객체


class Person:
    species = "human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"저는 {self.name}, {self.age}살입니다."

    def birthday(self):
        self.age += 1


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def introduce(self):
        return super().introduce() + f" {self.school}에 다닙니다."


p = Person("Charlie", 30)
print(p.introduce())
p.birthday()
print(p.age)

s = Student("Mina", 20, "서울대")
print(s.introduce())
print(isinstance(s, Person), Person.species)
