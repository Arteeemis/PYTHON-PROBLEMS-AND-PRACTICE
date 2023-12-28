def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        for item in items:
            if args[0] in item and item[args[0]] is not None:
                yield item[args[0]]
    else:
        for item in items:
            dict = {}
            all_none = True
            for key in args:
                if key in item and item[key] is not None:
                    dict[key] = item[key]
                    all_none = False
            if not all_none:
                yield dict

# Пример:
goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

print(str(list(field(goods, 'title')))[1:-1]) #должен выдавать 'Ковер', 'Диван для отдыха'
print(str(list(field(goods, 'title', 'price')))[1:-1]) #должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}




