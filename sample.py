print("Aljohn")

def adder():
    return ("congrtualations for finnishing python part 1")

List = ["apple","banana","cherry"]
Tuple = ("apple","banana","cherry")
Set = {"apple","banana","cherry"}

List[0] = "banana"
Set.remove("banana")
Set.update(['car'])
Set.add("Theo")
print(List[0])
print(Tuple[0])
print(Set)

print(adder())

i = 1 
while i < 5:
    print(i)
    if i == 3:
     break
    i+=1