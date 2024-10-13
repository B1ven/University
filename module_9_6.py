def all_variants(text):
    res = []
    for c in range(len(text)):
        for q in range(c + 1, len(text) + 1):
            res.append(text[c:q])
    yield '\n'.join(res)


a = all_variants("abc")
for i in a:
    print(i)
