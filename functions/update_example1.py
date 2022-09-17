


def simple_intrest(p:int, r: int, t: int): 
    return (p * r * t)/ 100

def compound_intrest(p, r, t):
    return p * (1 + r / 100) ** t

if __name__== "__main__":
    # simple use
    p = 10000
    r = 5
    t = 3
    si = simple_intrest(p, r, t)
    ci = compound_intrest(p, r, t)
    print(f'Simple Intrest is {si}')
    print(f'Compound Intrest is {ci}')

    # sample use 2
    p = float(input("Enter the principle: "))
    r = float(input("Enter the rate of intere: "))
    t = float(input("Enter the time: "))
    si = simple_intrest(p, r, t)
    ci = compound_intrest(p, r, t)
    print(f'Simple Intrest is {si}')
    print(f'Compound Intrest is {ci}')
