items = [
    ("Mosh", 100),
    ("Brad", 90),
    ("Ahmed", 10),
]


def smart_function(items):
    return items[1]


items.sort(key=smart_function, reverse=True)
print(items)
