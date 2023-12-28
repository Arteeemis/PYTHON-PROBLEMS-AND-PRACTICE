from random import randint
def gen_random(num_count, begin, end):
    ans = []
    for i in range(num_count):
        ans.append(randint(begin,end))
    yield ans

print(str(list(gen_random(5,1,3)))[1:-1])