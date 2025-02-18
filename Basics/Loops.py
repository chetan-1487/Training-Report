# For loop

for i in range(1,5):
    for j in range(i):
        print("*",end=' ')
    print("\n")


li=["Apple",2,"Banana"]
for i in li:
    print(i)


s="Hello world"
for ch in s:
    print(ch)


for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


# While loop

cnt=0
while(cnt<5):
    print("Hello")
    cnt=cnt+1