file=open("Hello.txt","w")
file.write("My name is Chetan and I am an AI Developer at thinkSys.")

file=open("Hello.txt","r")
content=file.read()
print(content)

with open("Hello.txt","r") as file:
    content=file.read()
    print(file.tell())
    print(content)
file.close()