#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N=int(input())
kolvo=0
A=[]
for i in range (N):
    a=int(input())
    A.append(a)
X=int(input())
diff=[]
for i in range (N):
    if A[i]==X:
        print (A[i])
    else:
        diff.append(abs(X-A[i]))
min_diff=100  #ограничение в значении чисел в массиве
position=0
for j in range (N):
    if diff[j]<min_diff:
        min_diff=diff[j]
        position=j
print (A[position])