import random
def F(names, N):
    global randomlist
    randomlist=[]
    for i in range (1,N+1):
        randomlist.append(random.choice(names))
    print(randomlist)
    return randomlist

def test_1_F():
    assert F(['John', 'Maria', 'Anna'], 3) != ['John', 'Maria', 'Anna']

def test_2_F():
    assert F(['John', 'Maria', 'Anna'], 10) != F(['John', 'Maria', 'Anna'], 10)