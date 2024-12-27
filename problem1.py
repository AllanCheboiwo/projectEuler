sol=[]
def problem1(m,n,lim):
    if(n>=lim):
        return 0
    else:
        sol.append(n)
        problem1(m,n+m,lim)
def main():
    problem1(5,5,1000)
    problem1(3,3,1000)
    final = set(sol)

    print(sum(final))


main() 