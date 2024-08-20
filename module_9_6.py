def all_variants(text):
    combs_ = len(text)
    for i in range(1, combs_ + 1):
        for start in range(combs_ - i + 1):
            yield text[start:start + i]


a = all_variants("abc")
for i in a:
    print(i)
