from bai2 import check_prime

arr = []
print(type(arr))
n = int(input("Enter n: "))
for i in range(n):
    x = int(input("Enter a[%d]: " % i))
    arr.append(x)

print("a = ", arr)
# sum = 0
# prime = []
# for i in arr:
#     sum += i
#     if check_prime(i):
#         prime.append(i)
# print("Sum = ", sum)
# print("Prime numbers in the array: ", prime)

# # Thêm 1 phần tử mới vào mảng
# arr.append(int(input("Enter a new element:")))
# print("New array: ", arr)

# # Xoá phần tử thứ k của mảng a
# k = int(input("Enter index k to delete:"))
# if 0 <= k < len(arr):
#     arr.pop(k)
#     print("Array after deleting element at index %d: " % k, arr)

# k = int(input("Enter index k: "))
# if 0 <= k < len(arr):
#     for i in arr:
#         if k == arr[i]:
#             print("Found k at index %d" % i)
#             break
# else:
#     print(f"index {k} not found in the array")
value = int(input("Enter value to delete: "))
for i in arr:
    if value == arr[i]:
        arr.pop(i)
        break
print("a = ", arr)

