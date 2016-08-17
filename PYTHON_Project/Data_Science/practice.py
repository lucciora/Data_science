class Animal():
    def __init__(self, name, age):
        self.name= name
        self.age = age
        
    def grrr(self):
        return "grrr"
    
class Dog(Animal):
    def __init__(self, name, age, owner):
        Animal.__init__(self, name, age)
        self.owner = owner
        
    def grrr(self):
        return "hi"

myDog = Dog("Kevin", 2, "jung")
print(myDog.grrr())


# Person 클래스를 만들고, 이것을 상속하는 학생 클래스를 만든다
# Person 클래스의 변수는 이름, 나이, 성별
# Student 클래스에는 이름, 나이, 성별, 학번 이 필요
# 부모 클래스에 add()메서드를 사용해서 10과 20을 더하는 Student 객체를 만드시오.
class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def talk(self):
        return "hi"
    
class Student(Person):
    def __init__(self, name, age, gender, id):
        Person.__init__(self, name, age, gender)
        self.id = id
        
myStudent = Student("joker", 21, "male", 21304)
print(myStudent.talk())