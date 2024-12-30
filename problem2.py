def fib(n):
    num = [1,2]
    count = 0
    while(num[count]+num[count+1]<=n):
        num.append(num[count]+num[count+1])
        count = count +1
    sum = 0
    for i in num:
        if i%2==0:
            sum= sum+i
    return sum

def main():
    print(fib(4000000))

main()

