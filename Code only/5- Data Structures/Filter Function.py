items = [
    ("Mosh", 100),
    ("Brad", 90),
    ("Ahmed", 10),
]

ratings = list(filter(lambda items: items[1] >= 20, items))
print(ratings)
