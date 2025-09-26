import numpy as np

# vector hoá
# a = np.array([1, 2, 3])
# print(a * 2)
# print(type(a))

# tạo arr random (kiểu int)
# x = np.random.randint(1, 10, size=10)
# y = np.random.randint(1, 10, size=10)
# print(x)
# print(y)
# print("Cộng 2 vector: ",x + y)

# print("Nhân 2 vector: ",x * y)

# a = np.random.randint(1, 5, size=(3, 3))
# b = np.random.randint(1, 5, size=(3, 3))
# print("Ma trận A:") 
# print(a)
# print("Ma trận B: ")
# print(b)

# print("Cộng 2 ma trận:", a + b)
# print("Nhân 2 ma trận:", a * b)
# print("Matmul:", a @ b)

# print("Tích vô hướng: ",np.dot(a, b))

# Tạo ma trận đơn vị 
# a1 = np.eye(5, 5)
# print(a1)
# print()
# # Chuyển vị ma trận
# a = np.arange(12)
# print(a) 
# print("Sử dụng hàm np.reshape()")
# print(a.reshape(3, 4))
# print("Sử dụng '-1': ")
# print(a.reshape(3, -1)) # -1 chỉ được xài 1 lần
# print()
# a2 = np.random.randint(1, 5, size=(2, 3))
# print("Sử dụng hàm np.transpose()")
# aT = np.transpose(a2)
# print(a2)
# print()
# print(aT)

# a3 = np.array([1, 2, 3])
# a4 = np.array([4, 5, 6])

# c = np.concatenate((a3, a4))

# x = np.array([[1,2], [3,4]])
# y = np.array([[5,6]])
# c1 = np.concatenate((x, y), axis=0) # cột bằng nhau nên chạy được
# print(c1)
# print()
# # c2 = np.concatenate((x, y), axis=1) # báo lỗi : vì hàng không bằng nhau
# # print(c2)
# y2 = np.array([[5], [6]])
# c3 = np.concatenate((x, y2), axis=1)
# print(c3)


# a = np.arange(9)
# # tham số là 3
# split_a = np.split(a, 3)
# print(split_a)
# # tham số là [3, 7]
# split_b = np.split(a, [3, 7])
# print(split_b)

# a = np.array([1, 2, 2, 3, 4, 4, 4, 5])
# print(np.unique(a))

# a = np.array([10, 20, 30, 40, 50])
# idx = np.where(a > 25) # Lấy vị trí các phần tử > 25
# print(idx)        # (array([2, 3, 4]),)
# print(a[idx])     # [30 40 50]

# b = np.array([10, 20, 30, 40, 50])

# res = np.where(b > 25, b*2, -1) # Nếu > 25 thì lấy b*2, ngược lại lấy -1

# print(res)
# # [-1 -1 60 80 100]

A = np.array([[4, -2], [1,  1]])
w, v = np.linalg.eig(A)
print("Giá trị riêng: ", w)
print("Vector riêng:")
print(v)