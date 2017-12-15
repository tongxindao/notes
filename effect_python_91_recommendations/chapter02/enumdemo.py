li = ['a', 'b', 'c', 'd', 'e']
mylist = list(enumerate(li, start=1))

print(mylist)
print("=" * 50)
print(mylist[::-1])
print("=" * 50)

personinfo = {'age': '26', 'hobby': 'football', 'name': 'John'}
for k,v in enumerate(personinfo):
    print(k, v)
print("=" * 50)
for k,v in personinfo.items():
    print(k,":",v)

