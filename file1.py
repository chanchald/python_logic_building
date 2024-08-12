# a classic problem to understand of loop

def you_me(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i%5 == 0:
            print('you_me')
        elif i % 3 == 0:
            print('you')
        elif i % 5 == 0:
            print('me')
        else:
            print(i)

you_me(100)