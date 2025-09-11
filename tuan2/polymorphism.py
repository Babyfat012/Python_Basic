# tính đa hình: các method cùng tên nhưng khác hành vi dựa trên đối tượng gọi chúng

# compile-time: giai đoạn trước khi chạy chương trình, compiler sẽ dịch code từ nnlt sang ngôn ngữ máy
# run-time: giai đoạn chương trình đã biên dịch xong, đang chạy trên máy 
# override: ghi đè phương thức = lớp con định nghĩa lại phương thức ở lớp cha (run-time polymorphism)
# overload là các hàm trùng tên nhưng khác tham số = lớp con sử dụng hàm với tham số truyền vào là gì (compile-time polymorphism)
# run-time polymorphism
class Dog:
    def sound(self):
        print("dog sound")

class Labrador(Dog):
    def sound(self):
        print("Labrador woofs") # ghi đè (override) lớp cha

class Beagle(Dog):
    def sound(self):
        print("Beagle barks") # ghi đè lớp cha

# compile-time polymorphism
class Calculator:
    def add(self, a, b = 0, c = 0): # overload
        return a + b + c

dogs = [Dog(), Labrador(), Beagle()]

for dog in dogs:
    dog.sound()

calc = Calculator()
print(calc.add(2))           # 2
print(calc.add(2, 3))        # 5
print(calc.add(2, 3, 4))     # 9

