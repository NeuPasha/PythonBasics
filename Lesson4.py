import random
import pandas as pd
def F(names, N):
    global randomlist
    randomlist=[]
    for i in range (1,N+1):
        randomlist.append(random.choice(names))
    print(randomlist)
    return randomlist

F(['Ivor', 'Harry', 'Benjamin', 'Lawrence', 'Archie', 'Lester', 'Johnnie', 'Roland', 'Charley', 'Horace', 'Ira', 'William', 'Owen', 'Willie', 'Curtis', 'Martin', 'Fred', 'Edmund', 'Henry', 'Andrew'], 100)

def most_frequent(list):
    print('Cамое частое имя: ',max(set(list), key = list.count))

most_frequent(randomlist)

def rarest_letter(list):
    letters_list=[]
    for i in range(0, len(list)):
        letters_list.append(list[i][0])
    print('Самая редкая первая буква:', min(set(letters_list), key = letters_list.count))

rarest_letter(randomlist)

logfile = pd.read_csv('log.txt', delimiter=' - ', index_col=[0], header=None, engine='python').sort_index(ascending=False)
print('Самый поздний лог:\n', logfile.iloc[0])

