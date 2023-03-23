num=int(input("please give a number. "))
def check_prim(number):
    is_prime=True
    for n in range(2,number):
        if number%n==0:
            is_prime=False
    if is_prime:
        print("its a prime number")
    else:
        print("its not a prime number")
check_prim(number=num)
