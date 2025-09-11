# tinh ke thua : lop con ke thua lop cha --> tang tinh tai su dung
class Dog:
    def __init__(self, name):
        self.name = name
    
    def display_name(self):
        print("Dog name:", self.name)

class Labrador(Dog):  # kế thừa đơn
    def sound(self):
        print("Labrador woofs")

class GuideDog(Labrador): # kế thừa đa cấp
    def guide(self):
        print(f"{self.name} Guides the way!")

class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenDog(Dog, Friendly): # kế thừa nhiều lớp
    # hàm overwrite từ lớp Dog
    def sound(self):
        print("Golden Dog barks")

lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()
# guide_dog.sound()

retriever = GoldenDog("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()