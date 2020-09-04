print('Hello Github')
print("silvia")
print(1+2-5*0/1)
print("today is a ", end= "")
print("sunny day")
print("would you like a tea?\nyes")

print("hello world")
print(1+2+5)
print("this is my first program")
print("hahaha")
print("world")
print(1)
print(3.14)
print(3e30)
print(1+2*3)
print(2>5)

print("hello",end="w")
print("hello",end="e")
print("hello","world","python","crossin")
print("hello\nworld\npython\ncrossin")
print("He said,\"I\'m yours!")
print("\\_v_//")
print("Stay hungry,\nstay foolish.\n\t    --Steve Jobs")

print(123&456)
eval(input())
name = input("what's your name:")
age = input("How old are you?")
print("hi,", name, ".")
print("you are" ,age, "years old.")
num1 = 10
print("num1=",num1)
num2 = int(input("num2:"))

print("num1>num2?",num1>num2)
print("num1<num2?",num1<num2)
print("num1=num2?",num1==num2)

bingo = False      #输出True
if bingo == False:
    print(True)
else:
    print(False)

b = 3          #输出False
if b - 3:
    print(True)
else:
    print(False)


x = input('请输入内容') #输出False
if x:
    print(True)
else:
    print(False)

a = True
b = not a  
print(b)  #输出False
print(not b) #输出True
print(a == b) #输出False
print(a != b)#输出True
print(a and b)#输出False
print(a or b)#输出True
print(1<2 and b==True)#输出False


m=0  #猜数字游戏
k=0
j="yes"
while j=="yes":
    m=m+1
    n=0
    from random import randint 
    num=randint(1,100)
    print("Guess what I think?")
    while True:
        n=n+1
        answer=int(input("tip:number from 1 to 100\n"))
        if answer<0:
            print('Exit game...')
            break
        elif answer>num:
            print("too big!")
        elif answer<num:
            print("too small!")
        else:
            print(str(n)+"times,BINGO!")
            break
    k=k+n
    avg=k/m
    print("average times:"+str(avg)+"\nWould you like again?")
    j=input("yes or no?")

a=1 #1-100求和
b=1
while a<100:
    a=a+1
    b=b+a
print(b)

a=0  #输出1到100的数字
b=1
while b<101:
    print(b)
    b=b+1
print("")

# 输出 1 到 10，但不输出 4 和 5
count = 0
while count<10:
    count += 1
    if count==4 or count==5:
        continue
    print(count)


# 100以内所有3的倍数的和
count=0
sum_3=0
while count<100:
    count=count+1
    if count%3==0:
        sum_3=sum_3+count
        print(count)
print(sum_3)

a=1  #输出首项为1的等比数列的前10项
b=int(input("请输入等比数列的公比:"))
for c in range(1,10):
    print(a)
    a=a*b


a='hello,world'#字符串格式转换
b=1.414
c=(1!=2)
d=(True and False)
e=(True or False)
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
print("a:%s;b:%.2f;"%(a,b)+"c:"+str(c)+";d:"+str(d)+";e:"+str(e))
print('\'hello,world\'\n\\\"hello,world\"')

name=input("name:") #字符串格式转换
age=input("age:")
gpa=input("gpa:")
result="%s,age:%s,GPA:%s"%(name,age,gpa)
print(result)

age=int(input())  #if控制流
if age>=18:
    print("你是个成年人了！")

a=int(input())  #if,else控制流
if a==1:
    print('one')
elif a==2:
    print('two')
elif a==3:
    print('three')
else:
    print('too many')

from random import randint   #if,else控制流
num=randint(0,100)
answer=int(input())
if answer<num:
    print('too small!')
elif answer>num:
    print('too big!')
else:
    print('BINGO!')


x=int(input('请输入横坐标的值：'))  #if,else控制流
y=int(input('请输入纵坐标的值：'))
if x>=0:
    if y>=0:
        print('第一象限')
    else:
        print('第四象限')
else:
    if y>=0:
        print('第二象限')
    else:
        print('第三象限')

for i in range(0,5):  #for循环
    print('*')

for i in range(0,5):
    print('*',end="")


for i in range(0,5):  #for循环嵌套,二叉树
    for j in range(0,5):
        print(i,j)

for i in range(0,5):    #for循环嵌套,*的5*5矩阵
    for j in range(0,5):
        print('*',end='')
    print()

for j in range(0,5):     #for循环嵌套,*的三角形
    for i in range(0,j+1):
        print('*',end='')
    print()

i=0                        #for循环嵌套,4-7
while i<5:
    i+=1
    for j in range(3):
        print(j)
        if j==2:
            break
    for k in range(3):
        if k==2:
            continue
        print(k)
    if i>3:
        break
    print(i)

for k in range(4):   #for循环嵌套,continue和break
    if k==2:
        continue
    print(k)


for k in range(4):
    if k==2:
        break
    print(k)

for i in range(1, 10): #九九乘法表
    for j in range(1,i+1):
        print('%d x %d = %d' %(j,i,i*j),end=' ')
    print()

for i in range(1,5):  #1,2,3,4 四个数字，组成互不相同且无重复数字的三位数
    for j in range(1,5):
        if i==j:
            continue
        for k in range(1,5):
            if j==k:
                continue
            elif i==k:
                continue
            print(i,j,k)


h=float(input('请输入你的身高M:'))#BMI
w=int(input('请输入你的体重KG:'))
BMI=w/h**2
if BMI<18.5:
    print('BMI:'+str(BMI)+' 体重偏轻')
elif BMI<24:
    print('BMI:'+str(BMI)+' 体重正常')
else:
    print('BMI:'+str(BMI)+' 体重偏重')



def sayhello(someone="world"):#定义和调用函数
    print(someone,"says Hello!")
sayhello("lili")
sayhello()

def plus(num1,num2=6):
    print(num1+num2)
    x=num1+num2
    return x
    
plus(9,45)
plus(9)
x=plus(3,4)
y=x*5
print(y)

def get_pi():
    pi=3.14
    return pi
x=get_pi()
print(x)

def double(a):
    return a*2
x=3
y=double(x)
print(y)


x=print(123)
print(x)

def isEqual(num1,num2):#猜数字游戏，函数版
    if num1<num2:
        print('too small')
        return False
    if num1>num2:
        print('too big')
        return False
    if num1==num2:
        print('bingo!')
        return True
from random import randint
num=randint(1,100)
print('Guess what I think?')
bingo=False
while bingo==False:
    answer=int(input())
    bingo=isEqual(answer,num)

import math   #(-b±√(b²-4ac))/2a
def A(a,b,c):
    d=(-1*b+math.sqrt((math.pow(b,2)-4*a*c)))/2*a
    e=(-1*b-math.sqrt((math.pow(b,2)-4*a*c)))/2*a
    print(e)
    print(d)
A(1,4,2)

def rectangle(l=5,w=5):#*矩阵，函数版
    for i in range(0,l):
        for j in range(0,w):
            print('*',end='')
        print()
rectangle(3)
rectangle(w=3)

print(list(range(1,10)))

arr=[2,4,6,8,10]
for i in arr:
    print(i)
print(arr)

a='python' #列表，字典
for i in a:
	print(i)
	
score = {'萧峰': 95,'段誉': 97,'虚竹': 89}
for name in score:
    print (score[name])

arr=[1,1,1,3,3,5,7,7]
s=set(arr)
arr=list(s)
print(arr)

list_1=list(range(1,101))#字符串和list转换
print(list_1)
list_2=[str(x)for x in list_1 if(x%2==0 or x%3==0 or x%5==0)]
print(list_2)
num_1=';'.join(list_2)
print(num_1)

arr=[365, 'everyday', 0.618, True,]
arr.append([2,7])
print(arr)

list_s = ['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit', 'is', 'better', 'than', 'implicit']#统计列表中每个单词出现的次数
dict_1={}
for s in list_s:
    if s not in dict_1:
        dict_1[s]=1
    else:
        num1=dict_1.get(s)
        num1=num1+1
        dict_1[s]=num1
print(dict_1)

import string  #生成优惠券号码
str1=string.ascii_letters
lst1=list(str1)
lst3=[]
for i in range(0,200):
    import random
    lst2=random.sample(lst1,8)
    if lst2 not in lst3:
        lst3.append(lst2)
    print(''.join(lst3[i]))


lst_1=['黑桃','红桃','金花','方块']#发牌程序
lst_2=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
lst_3=['大王','小王']
for i in lst_1:
    for j in lst_2:
        str_1=''.join([i,j])
        lst_3.append(str_1)
import random
random.shuffle(lst_3)
x=0
poker_1=[lst_3[0+x*3]]
poker_2=[lst_3[1+x*3]]
poker_3=[lst_3[2+x*3]]
poker_4=lst_3[51:54]
for x in range(1,17):
    poker_1.append(lst_3[0+x*3])
    poker_2.append(lst_3[1+x*3])
    poker_3.append(lst_3[2+x*3])
print(poker_1)
print(poker_2)
print(poker_3)
print(poker_4)

with open(r'e:\实验.txt')as f_1: #文件读取
    print(f_1.readlines())

f_1=open(r'e:\test.txt','w')  #从控制台输入一些内容，保存至一个文件
f_1.write('I will be in a file.\nSo cool!')
f_1.close()

f_2=open(r'e:\实验.txt')
con_1=f_2.read()
f_2.close()
f_1=open(r'e:\test.txt','w')  #从控制台输入一些内容，保存至一个文件
f_1.write(con_1)
f_1.close()

with open('e:/test.txt',encoding='utf-8')as scores:#文件的读写，原文件n行，开分为n个文件，每个文件1行内容
    lines=scores.readlines()
    print(lines)
    i=0
    for line in lines:
        print(line)
        i+=1
        filename='e:/text2_%d.txt'%i
        with open( filename,'w',encoding='utf-8')as exp:
            exp.write(line)

try:#文件读写异常处理
    with open('e:/test.txt',encoding='utf-8')as file_1:
        print(file_1.read())
        a=int('0.5')
        print(3)
        import yyy
        print(4)
except IOError as e_io:
    print('io error',e_io)
except ValueError as e_val:
    print('value error',e_val)
except Exception as e:
    print('error',e)
else:
    print('success')
finally:
    print('end')

scores=open('e:/test.txt',encoding='utf-8')#成绩求和
lines=scores.readlines()
print(lines)
scores.close()
results=[]
for line in lines:
    print(line)
    score=line.split()
    print(score)
    sum=0
    for i in score[1:]:
        sum=sum+int(i)
    result='%s\t:%d\n'%(score[0],sum)
    print(result)
    results.append(result)
    print(results)
    output=open('e:/results.txt','w',encoding='utf-8')
    output.writelines(results)
    output.close()

#1
sum=0
for n in range(1,101):
    if n%3==0:
        sum=sum+n
        print(n)
    else:
        continue
print(sum)

#2
h=input('请输入矩形的高：')
w=input('请输入矩形的宽：')
for i in range(0,int(h)):
    for j in range(0,int(w)):
        print('*',end=' ')
    print()


#4
nums = [23, 45, 8, 13, 50, 43, 21]
sum = 0
for n in nums:
    sum=sum+n
    if sum > 100:
        break
print(sum)


with open('e:/实验.txt',encoding='utf-8')as forb:
    list_1=forb.readlines()
    print(list_1)
cont=input('请输入需要查询的内容：')
for word in list_1:
    if word in cont:
        print(cont.replace(word,'*'))
    else:
        print(1)


def swap(cont): #屏蔽词替换 
    with open('e:/实验.txt',encoding='utf-8')as forb:
        list_1=forb.readlines()
    list_2=[]
    for word in list_1:
        newword=word.strip('\n')
        if newword in cont:
            cont=cont.replace(newword,'*'*len(newword))
    print(cont)
#4.附加题1：示例中如果英文屏蔽词和输入字符的大小写不匹配，是无法替换掉的。如何既能忽略大小写进行屏蔽，又能保证其他字母的大小写正常？（提示：需要手动增加大小写转换）
#5.附加题2：如果“仙人”是屏蔽词，则会把“仙人掌”误判为“**掌”。想减少误判率，可使用分词库改进方法，最常用的中文分词库是 jieba 分词库。




    

