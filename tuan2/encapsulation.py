# tính đóng gói, bao gồm; 
# public: truy cập từ bất cứ đâu
# private: chỉ truy cập trong class
# protected: truy cập trong class và subclass

class Dog:
    def __init__(self, name, breed, age):
        self.name = name # thuộc tính public
        self._breed = breed # thược tính protected 
        self.__age = age # thuộc tính private

    # phương thức public
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"
    
    # getter / setter
    def get_age(self):
        return self.__age
    
    def set_age(self ,age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

dog = Dog("Buddy", "Labrador", 3)

print(dog.name)

print(dog._breed)

# print(dog.__age) # error

print(dog.get_age())

dog.set_age(5)
print(dog.get_info())