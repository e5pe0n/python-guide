fruits = {
    "apple": 100,
    "banana": 200,
    "orange": 300,
    "grape": 400,
}

my_wish_list = ["apple", "orange"]


# imperative
shopping_cart = {}
for k, v in fruits.items():
    if k in my_wish_list:
        shopping_cart[k] = v
print(shopping_cart)    # {'apple': 100, 'orange': 300}


# comprehension style
shifted_box = {k: v for k, v in fruits.items() if k in my_wish_list}
print(shopping_cart)    # {'apple': 100, 'orange': 300}
