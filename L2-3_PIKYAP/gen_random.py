from random import randint
def gen_random(count, begin, end):
    ans = []
    for i in range(count):
        ans.append(randint(begin,end))
    return sorted(ans)

if __name__=="__main__":
    print(gen_random(5,1,3))
