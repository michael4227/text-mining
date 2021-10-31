from thefuzz import fuzz
a = open('text-mining/730-0.txt','r')
b = open('text-mining/730-1.txt','r')
book1=''
book2=''
for line in a:
    book1 += line
print(book1)
for line in b:
    book2 += line
print(book2)
c = 'ccc'
d = 'dcd'
e = 'aaa'
rext_similarity = fuzz.ratio(c,d,e)
text_similarity = fuzz.ratio(book1,book2)
print(rext_similarity)
print(text_similarity)
