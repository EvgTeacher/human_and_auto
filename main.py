class Counter:

    def __init__(self, max_number):
        self.i = -1
        self.max_number = max_number

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i

    def Generator(self):
        for _ in count:
            yield self.i + 1


count = Counter(9)
for i in count.Generator():
    print(i)

# for item in count:
#     print(item)

#
# print(count.__iter__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())