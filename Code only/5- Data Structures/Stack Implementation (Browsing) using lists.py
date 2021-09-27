browsing_history = []
browsing_history.append("www.google.com")
browsing_history.append("codewithmosh.com")
browsing_history.append("www.mlsa.pk")

browsing_history.pop()
browsing_history.pop()
browsing_history.pop()

# print(browsing_history[-1])
print(browsing_history)

if not browsing_history:
    print("disable")
