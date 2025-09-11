# python class
class Dog:
    # class attribute
    legs = 4

    # constructor
    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age

# instance of class Dog
# self là tham chiếu đến đối tượng đang gọi hàm
dog1 = Dog("Buddy", 3)  
dog2 = Dog("Charlie", 5) 

print(dog1.name, dog1.age, dog1.legs)  
print(dog2.name, dog2.age, dog2.legs)  
print(Dog.legs)  # access class attribute
print(Dog.name) # error

