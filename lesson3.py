
import pymorphy2
import pymorphy2_dicts
morph = pymorphy2.MorphAnalyzer()

textfile = open('text.txt', 'r')
textread = textfile.read()

znaki = ['.', ',', '!', '?','-','«','»','—','(',')',';',':']

text1 = textread.translate({ord(x): '' for x in znaki})
# print(text1)

text2 = text1.split()
# print(text2)

text3 = list(map(str.lower, text2))
# print(text3)

my_dict={}
for i in text3:
    my_dict[i] = text3.count(i)
# print(my_dict)

for i in text3:
    l=morph.parse(i)[0]
    # print(l.normal_form)

text4 = set(text3)
text5 = sorted((my_dict.items()), key=lambda x:x[1], reverse=True)
print('Количество разных слов:', len(text4))
print(text5[:5])
