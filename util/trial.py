'''pos=["a","b","c"]
for i in range(len(pos)):
    print(i)'''
'''arr=[1,2]
b=[]
c=[]
for a in arr:
    c.append(4)
    c.append(5)
    b.append(a)
for v in b:
    arr.remove(v)
for v in c:
    arr.append(v)
print(arr)'''
'''word="ice-skate"
if(word.find("ice")!=-1):
    print("found")
if(word[2]=='e'):
    print("yay")'''
class Emit:
    id="null"
    cnt=0
    def __init__(self, name):
        self.id = name
        self.cnt=1
    def frequency(self):
        return self.cnt
    def increase(self):
        self.cnt+=1

    def isID(self,name):
        if self.id==name:
            return True
        else:
            return False

alphabet=[]
for i in range(26):
    e=Emit("*&^$$)@^$")
    listy=[]
    listy.append(e)
    alphabet.append(listy)
for a in alphabet:
    for e in a:
        print(e.id)