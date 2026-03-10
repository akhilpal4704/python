def count(limit):
    n=0
    while n<limit:
        yield n
        n +=1

num = count(5)
print(next(num))
