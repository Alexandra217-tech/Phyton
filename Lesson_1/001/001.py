#Задача 2: Найдите сумму цифр трехзначного числа.
a = input()
sum=0
b=0
for i in range (len(a)):
    b=int(a[i])
    sum+=b
print (sum)