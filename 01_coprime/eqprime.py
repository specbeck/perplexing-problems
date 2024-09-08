import time

primes = [2, 3]

n = int(input("Enter the range: "))

start = time.time()

for i in range(1, n):
    primes.append(6*i + 1)
    primes.append(6*i - 1)

print(f"{primes}\nNumber of primes is {len(primes)}")

print(f'Time it took for the calculation {(time.time() - start):.2f}')
