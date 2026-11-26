#리스트 + 연산 (리스트+리스트), 중복허용
lang1=["c","c++","JAVA"]
lang2=["Python","Go","C#"]

langs=lang1+lang2

print(langs)


#최대값 ->max(), 최소값->min(),개수->ien()

nums=[1,2,3,4,5,6,7]
print("최대값:",max(nums),"최소값:",min(nums),"개수: "len(nums))

#리스트 합 -> sum()
print("리스트 요소의 합: "sum(nums))
print("리스트 평균:",sum(nums)//len(nums))



#리스트 중복을 허용 <-> sey()
#다음 두 리스트를 하나로 합친 후, 중복된 요소가 자동으로 재거되도록
#@@@에 들어갈 코드를 작성하시오
lang1=[1,2,3,4]
lang2=[1,2,3]
langs=set(lang1+lang2)
print(*langs)

#리스트 요소 중에 홀수만 출력
nums=[1,2,3,4,5,6,7,8,9,10]

for i in nums:
    if 1%2==1:
        print(i,end="")

#리스트 컴프리헨션
resert=[n for i in nums if n%2==1]

#join 메서드 리스트-> 문자열
#삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
interest=['삼성전자','LG전자','Naver','SK하이닉스','미래에셋대우']
print("/".join(interest))

#split 메서드 문자열 -> 리스트
string ="삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
interest1=string.split("/")
print(interest1)

#리스트 정렬 (오름차순, 내림차순)
data=[2,4,3,1,5,10,9]

data.sort(reverse=False) #오름차순 sort()
data.sort(reverse=True) #내림차순
print(data)

#sorted(리스트이름) ->sorted(리스트이름,reverse=True) <-내림차순
nums=[5,4,1,4,2]
result=sorted(reverse=True)

#
a,b,*c=0,1,2,3,4,5
print("a:",a,"b:",b,"c:",c)

#딕셔너리 key:value
#추가 -> dic이름["key"]=value
a={}
b=set() #집합
ice=["메로나":1000,"폴라포":1200,"빵빠레":1800)
ice["죠스바"]=1200
ice["월드콘"]=1500

#key에 해당하는 value 를 찾는다.
print(ice["key"]

#딕셔너리 요소 삭제
del ice["key"]

#딕셔너리 인덱싱 -> 메로나 가격 출력

#딕셔너리 keys() ->key에 집합
print(inventory.keys()) #리스트로 변환하려면 리스트로 형변환

#딕셔너리 values() -> value의 집합
print(inventory.values)


#함수 정의 def
def print_coin():
    print("비트코인")

#함수 호출 100번
    for _ in range(100):
        print_coin()

# 함수 안에 문자열 100번 출력
def print_coin1():
    print("비트 "*100)
print_coin1()

#함수에 인수를 전달 -> 함수이름("인수")
def func(a):
    print(a)

func("hello")

#하나의 문자열을 입력받아 뒤에:D 이거 붙이시오
def print_smile(string):
    print(string+":D")
    print_smile("안녕하세요")

#세개의 수를 입력받아 가장 큰 값 출력 함수
#삼항연산자를 사용
def max_val(a,b,c):
    max_v=a
    max_v=b if b > max_v else max_v #참 if 조건 alse 거짓
    max_v=c if c > max_v else max_v 
    return max_v

#하나의 딕셔너리를 입력받아 딕셔너리의 key의 값을
#화면에 출력하는 print_keys 함수를 정의 하라.
def print_keys(dic):
    for i in dic.keys():
        print(i)

print_keys({"이름":"김말똥","나이":30,"성별":0})


def my_print(a,b):
    print("왼쪽:",a)
    print("오른쪽:",b)

my_print(b=100,a=200)
#함수 -> 지역변수 (그안에서만 live)
def n_plus_1 (n):
    result=n+1

print(n_plus_1(3))




    





