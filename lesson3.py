
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

for i in text3:
    l=morph.parse(i)[0]
    # print(l.normal_form)

text4 = sorted(set(text3), reverse=True)
# print(text4[:5])
# print(len(text4))
