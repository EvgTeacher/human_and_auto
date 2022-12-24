# p = print
# print(p)
#
# def func():
#     pass
#
# print(func)

# def external():
#     a = 1
#     def inner():
#         print("A=", a)
#     return inner
#
# x = external()
# print(x)
# x()

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner
a1 = counter()
print(a1())
print(a1())
print(a1())
b1 = counter()
print(b1())
print(a1())
print(b1())