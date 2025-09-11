# tính trừu tượng: ẩn đi phần cài đặt, chỉ phơi bày phần cần thiết --> đảm bảo tính nhất quán
# python có module abc (Abstract Base Class)
# Dùng @abstractmethod để buộc các lớp con phải override lại phương thức đó
# Partial abstraction: gồm hàm abstract và hàm bình thường
# Full abstraction: chỉ gồm hàm abstract (giống interface java)
from abc import ABC, abstractmethod 

class Dog(ABC): # lớp abstract
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    def display_name(self):
        print(f"Dog name: {self.name}")

class Labrador(Dog):
    def sound(self):
        print("Labrador woofs!")
    
class Beagle(Dog):
    def sound(self):
        print("Beagle bark!")
    
dogs = [Labrador("Buddy"), Beagle("Charlie")]
for dog in dogs:
    dog.display_name()
    dog.sound()