def all_variants(text):
    for c in range(len(text)):
        for q in range(c + 1, len(text) + 1):
            yield text[c:q]


a = all_variants("abc")
for i in a:
    print(i)
