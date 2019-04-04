"""def sum_all(start, end, step=1):
    output=0
    for i in range(start, end+1, step):
        output += i

    return output

print("0 to 100:", sum_all(0, 100, 2))
print("0 to 1000:", sum_all(0, 1000))
print("0 to 50:", sum_all(0, 50))

def recursion_function(i=1) :
    print("안녕하세요")
    if(i < 10):
        recursion_function(i+1)

recursion_function(0)

def factorial(n):
    if n == 0:
        return 1
    elif n > 0 :
        return factorial(n-1)*n

print(factorial(5))

print(factorial(100))

def fibo(n):
    if n > 2:
        return fibo(n-1) + fibo(n-2)
    else:
        return 1

print(fibo(1))
print(fibo(5))
print(fibo(20))"""

dictionary = {
    1:1,
    2:1
}
def fibo(n):
    if n in dictionary:
        return dictionary[n]
    else : 
        output = fibo(n-1) + fibo(n-2)
        dictionary[n] = output
        return output

print(fibo(10))
print(fibo(50))
print(fibo(100))