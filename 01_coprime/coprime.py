import random

def main():
    primes = get_primes(100)
    alice, bob = generate_random_seed(100)

    print(f"{alice} and {bob} has prime factors == {check_factors(alice, bob, primes)}")

    



def check_factors(n1: int, n2: int, factors: list[int]) -> bool:
    """
    Checks for common factors between n1 and n2 
    """
    for num in range(2, max(n1, n2)):    
        for factor in factors:
            if (n1 % factor == 0 ) and (n2 % factor == 0):
                return True
    else:
        return False

def generate_random_seed(range: int) -> tuple[int, int]:
    """
    Generates random seed numbers based on the range
    """
    x = random.randint(1, range)
    y = random.randint(1, range)

    return x, y


def get_primes(n: int) -> list[int]:
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