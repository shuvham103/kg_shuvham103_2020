import sys

s1=str(sys.argv[1])
s2=str(sys.argv[2])
b=False
s1=list(s1)
s2=list(s2)
sets1=set(s1)

if (len(s1)==len(sets1)):

    if (len(s1)==len(s2)):
        b=True
print(s1)
print(s2)
print(b)



