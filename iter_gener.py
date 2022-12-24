# class Iter_Generete():
#     def __init__(self, number):
#         self.number = number
#         self.i = 0
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.number:
#             raise StopIteration
#         return self.i
#
#     def func(self):
#         for i in self:
#             yield i
#
# # def func(count):
# #     for i in count:
# #         yield i
#
#
# count = Iter_Generete(10)
#
# print(count.func())
# print(count.func().__next__())
# # print(count.func().__next__())
# for i in count.func():
#     print(i)

# def gener(b):
#     for i in b:
#         yield i
#
#
# a = [1, 2, 3, 4, 5, 6, 7]
# b = a.__iter__()
# print(gener(b).__next__())
def divider(a, b):
    try:
        if a < b:
            result.append(res)
        if b > 100:
            result.append(res)
        if type(a) == "str":
            result.append(res)
        if b == 0:
            raise ZeroDivisionError
    except IndexError:
        print('Error index')
    except ValueError:
        print('Error value')
    except TypeError:
        print('Error type')
        return
    except ZeroDivisionError:
        print('Error ZeroDivisionError')
        return
    return a / b



result = []

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
