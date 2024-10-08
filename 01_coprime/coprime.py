import random
import time

def main():

    start_time = time.time()

    n = int(input("How many times do you need to perform the experiment? "))

    alice, bob = count_wins(n)
    ap, bp = calculate_probabilities(alice, bob, n)
    
    print(f"Time taken for program: {time.time() - start_time}")


def write_to_csv(alice: int, bob: int, awin: bool, bwin: bool):
    """
    Writes results supplied to a file
    """
    with open("results.csv", 'w') as file:
        file.write(f"{alice},{bob},{awin},{bwin}")



def calculate_probabilities(a: int, b: int, ss: int) -> tuple[float, float]:
    """
    Calculates probabilities of winning based on the number of wins and the sample space
    """
    alice = (a/ss) * 100
    bob = (b/ss) * 100

    print(f"The probability of alice winning is {alice:.2f}% and bob winning is {bob:.2f}%")
    return (round(alice, 2), round(bob, 2))


def experiment_outcome(range: int) -> bool:
    """
    Performs the experiment on the range supplied, returns a boolean for prime factor
    """

    primes = get_primes(range)
    alice, bob = generate_random_seed(range)

    #print(f"{alice} and {bob} has prime factors == {check_factors(alice, bob, primes)}")
    result = check_factors(alice, bob, primes)
    write_to_csv(alice, bob, result, ~result)
    return result

    
def count_wins(iters: int) -> tuple[int, int]:
    """
    Counts wins for the number of iters supplied
    
    Returns a tuple with wins as (Alice, Bob)
    """
    alice_wins = 0
    for _ in range(iters):
        if experiment_outcome(100): # hardcodes the range here
            alice_wins += 1
    
    bob_wins = iters - alice_wins # Whenever alice loses, bob wins

    return alice_wins, bob_wins


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
