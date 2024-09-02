def main():
    print(get_primes(100))
    
def get_primes(n):
    """
    Returns a list of prime numbers upto n, the number specified
    """
    primes = []
    for num in range(2, n):
        for factor in range(2, num):
            if num % factor == 0:
                break
        else:
            primes.append(num)

    return primes

if __name__ == "__main__":
    main()