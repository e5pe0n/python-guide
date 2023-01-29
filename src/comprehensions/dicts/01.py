en2ja = {
    "dog": "いぬ",
    "cat": "ねこ",
    "cow": "うし",
}


# imperative
ja2en = {}
for k, v in en2ja.items():
    ja2en[v] = k
print(ja2en)
# {'いぬ': 'dog', 'ねこ': 'cat', 'うし': 'cow'}

# using comprehension
ja2en = {v: k for k, v in en2ja.items()}
print(ja2en)
# {'いぬ': 'dog', 'ねこ': 'cat', 'うし': 'cow'}
