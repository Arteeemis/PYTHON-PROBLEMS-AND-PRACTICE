from test import gen_random 

class Unique(object):
    def __init__(self, items, **kwargs):
        self.data = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.unique_items = set()

    def __next__(self):
        while True:
            item = next(self.data)
            check_item = item.lower() if self.ignore_case else item
            if check_item not in self.unique_items:
                self.unique_items.add(check_item)
                return item

    def __iter__(self):
        return self

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
unique_data = Unique(data)
print(list(unique_data))
# Output: [1, 2]

data = gen_random(10, 1, 3)
unique_data = Unique(data)
print(list(unique_data))
# Output: [1, 2, 3]

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
unique_data = Unique(data)
print(list(unique_data))
# Output: ['a', 'A', 'b', 'B']

unique_data_ignore_case = Unique(data, ignore_case=True)
print(list(unique_data_ignore_case))
# Output: ['a', 'b']
