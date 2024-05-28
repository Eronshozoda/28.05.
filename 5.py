tup1=(1,2,3,4)
tup2=(3,5,2,1)
tup3=(2,2,3,1)

sum_of_tuples=[]

for i in zip(tup1,tup2,tup3):
    sum_of_tuples.append(sum(i))
print(tuple(sum_of_tuples))