import time

def get_primes(n: int) -> list[int]:
    """
    Returns a list of prime numbers upto n, the number specified
    """
    primes = [2, 5]
    for num in range(2, n):
        
        if num % 2 == 0:
            pass
        if num % 3 == 0:
            pass
        if num % 5 == 0:
            pass
        
        if num % 10 in [1, 3, 7, 9]:
            for factor in range(2, num):
                if num % factor == 0:
                    break
            else:
                primes.append(num)

    return primes


def main():

    n = int(input("Enter the range you want: "))

    start = time.time()
    
    primes = get_primes(n)
    print(primes, len(primes))
    
    print(f"Time of execution is {(time.time() - start):.2f}")


if __name__ == "__main__":
    main()
