f = open("filrdir")
print("-------------------------------------------------")
f = f.readlines()
print(f)
print(type(f))

def one(file):
    a = 0
    c = []
    while a <= len(file)-1:
        b = ([file[a]])
        c.append(b)
        a += 1
    else:
        pass
    return c

a = one(f)

b = a[0][0]
print("b:", b)


def two(file):
    a = 0
    d = []
    while a <= len(file)-1:
        b = file[a][0]
        c = b.split(",")
        d.append(c)
        a += 1
    else:
        pass
    return d

import numpy as np

print(two(a))
z = np.array(two(a))
print(z)
print(z[0])
print(z[0][0])



# c = b.split(",")
# print(c)
# print(c[0])



# class make:
#     def __init__(self, mentor, name, sex, phone, email, birth, major):
#         self.mentor = mentor
#         self.name = name
#         self.sex = sex
#         self.phone = phone
#         self.email = email
#         self.birth = birth
#         self.major = major
#
#         self.info = [self.mentor, self.name, self.sex, self.phone, self.email ,self.birth, self.major]
#         print(self)
#
# make(1,2,3,4,5,6,7).info

# for i in range(30):
#     f.pop()
#     print(f.pop())

# f.pop()
# print(f.pop())
# f.pop()
# print(f.pop())
# f.pop()
# print(f.pop())

# for i in range(30):
#     b = list(a.readline())
#     b = b.append
#
#
# print(info(f))
