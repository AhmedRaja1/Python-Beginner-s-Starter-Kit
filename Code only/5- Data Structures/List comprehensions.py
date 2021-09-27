items = [
    ("Mosh", 100),
    ("Brad", 90),
    ("Ahmed", 10),
]

ratings = [items[1] for items in items]  # Map Alternative
ratings = [items[1] for items in items if items[1] >= 20]  # Filter Alternative
print(ratings)
