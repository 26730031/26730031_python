#set
b=[1,2,3,1,2,3,1,2,3]
a=set(b)
print(*a)

#len() 개수 반환
fruits={"apple","banana","grape"}
size=len(fruits)
print(size)

# in 포함되는지
fruits={"apple","banana","grape"}
if "apple" in fruits:
    print("apple 있습니다.")
else:
    print("없습니다.")

#출력(저장된 순서가 없다)
fruits={"apple","banana","grape"}
print(fruits)

#출력 (출력시 정렬해서 출력할 수는 있다)
fruits={"apple","banana","grape"}
for x in sorted(fruits,reverse=True):
    print(x,end=" ")
    
#add() 요소 추가
fruits={"apple","banana","grape"}
fruits.add("kiwi")
print(fruits)
fruits.remove("kiwi")
print(fruits)
fruits.clear()
print(fruits)
