"""
--------------------------------------
 NUMPY EXAMPLES BASED ON SLIDES 📌
 Author: Long Phát
--------------------------------------
"""

import numpy as np

print("\n================= 1. TẠO MẢNG =================")

# np.array() từ list
arr = np.array([1, 2, 3, 4])
print("np.array:", arr)

# Tạo mảng dạng range
arange_arr = np.arange(0, 10, 2)
print("np.arange:", arange_arr)

# zeros và ones
zeros_arr = np.zeros((2, 3))
ones_arr = np.ones((2, 2))
print("np.zeros:\n", zeros_arr)
print("np.ones:\n", ones_arr)


print("\n================= 2. THAO TÁC MẢNG =================")

# Reshape
reshaped = np.arange(12).reshape(3, 4)
print("Reshape 3x4:\n", reshaped)

# Transpose
print("Transpose:\n", reshaped.transpose())

# Concatenate
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
concat_arr = np.concatenate((a, b))
print("Concatenate:", concat_arr)

# Split
split_arr = np.split(np.arange(9), 3)
print("Split:", split_arr)


print("\n================= 3. THỐNG KÊ =================")

data = np.array([1, 1, 2, 3, 3, 3, 4, 5, 5])
print("Mean:", np.mean(data))

hist, bins = np.histogram(data, bins=5)
print("Histogram:", hist)
print("Bins:", bins)


print("\n================= 4. ĐẠI SỐ TUYẾN TÍNH =================")

A = np.array([[1, 2], [3, 4]])

print("Matrix A:\n", A)
print("Det(A):", np.linalg.det(A))
print("Inv(A):\n", np.linalg.inv(A))
print("A @ A (np.matmul):\n", np.matmul(A, A))

# Dot product
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print("Dot(v1,v2):", np.dot(v1, v2))

# Eigenvalues & eigenvectors
eig_val, eig_vec = np.linalg.eig(A)
print("Eigenvalues:", eig_val)
print("Eigenvectors:\n", eig_vec)


print("\n================= 5. TÌM KIẾM / LỌC =================")

x = np.array([10, 20, 30, 40, 50])
print("Các phần tử > 25:", x[np.where(x > 25)])

# np.where(condition, true, false)
cond_res = np.where(x > 25, x * 2, -1)
print("np.where():", cond_res)

# Unique values
u, idx = np.unique(data, return_index=True)
print("Unique values:", u)
print("Index xuất hiện đầu tiên:", idx)


print("\n================= 6. TẠO DỮ LIỆU MÔ PHỎNG =================")

lin = np.linspace(0, 1, 5)
print("np.linspace:", lin)

poly = np.polyfit([0, 1, 2, 3], [1, 2, 3, 5], 1)
print("np.polyfit:", poly)


print("\n================= END =================")
print("✔ File chạy thành công!")
