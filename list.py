import numpy as np
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [a+b for a in lowercase for b in digits]
# print(answer[:10])

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [
    a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50]  # Display first 50 ids
old = np.array([[1, 1, 1],
                [1, 1, 1]])
new = old
new[0, 0:2] = 0
print(new)
A1 = ["A", "B", "C"]
B1 = [1, 2, 3]
print(A1+B1)
A1 = 4
# type(lambda(A1: A1+B1))
n = np.array([1, 2, 3, 4, 5, 3, 4, 6, 7])
print(n)
s = n.reshape(3, 3)
print(s)
x =
