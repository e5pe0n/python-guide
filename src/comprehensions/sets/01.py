shopping_cart = [
    {
        "name": "apple",
        "price": 100,
    },
    {
        "name": "orange",
        "price": 200,
    },
    {
        "name": "orange",
        "price": 200,
    },
    {
        "name": "grape",
        "price": 300,
    },
    {
        "name": "apple",
        "price": 100,
    },
]


# imperative
# Don't write `{}` for empty sets; `{}` is the notation for empty dict
fruits = set()
for item in shopping_cart:
    fruits.add(item["name"])
print(fruits)   # {'apple', 'orange', 'grape'}


# comprehension style
fruits = {item["name"] for item in shopping_cart}
print(fruits)   # {'apple', 'orange', 'grape'}
