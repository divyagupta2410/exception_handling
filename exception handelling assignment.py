#1.
def funct():
    try:
        d=5/0
        print(d)
    except Exception as e:
        print("",e)
funct()


#2.
subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
x=[s+" "+v+" "+o+"." for s in subjects for v in verbs for o in objects]
for i in x:
    print(i)
