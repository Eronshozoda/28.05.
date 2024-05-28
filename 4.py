
my_tupl=('i','n','d','e','x', " ", 't','u','p','l','e')
e=input()
if e in my_tupl:
    print(f'My element ({e}) in ({my_tupl.index(e)})  index a tuple')
else:
    print(False)
