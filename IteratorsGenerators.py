class FlatIterator:
    def __init__(self, root):
        self.out_start = 0
        self.out_end = len(root)
        self.in_start = 0
        self.in_end = None
        self.step = 1
        self.root = root
        self.out_cur = None
        self.inner_cur = None

    def __iter__(self):
        self.out_cur = self.root[self.out_start]
        self.in_end = len(self.out_cur)
        return self

    def __next__(self):
        if self.in_start >= self.in_end:
            self.out_start += self.step
            if self.out_start >= self.out_end:
                raise StopIteration
            self.out_cur = self.root[self.out_start]
            self.in_end = len(self.out_cur)
            self.in_start = 0

        self.inner_cur = self.out_cur[self.in_start]
        self.in_start += self.step

        return self.inner_cur


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]

for item in FlatIterator(nested_list):
    print(item)

print('*' * 100)


def flat_generator(nested_list):
    for n in nested_list:
        for a in n:
            if type(a) is list:
                yield from flat_generator(a)
            else:
                yield a


for item in flat_generator(nested_list):
    print(item)
