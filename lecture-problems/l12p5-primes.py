def genPrimes():
    primes = []
    last = 1
    while True:
        last += 1
        if all([(last % p) != 0 for p in primes]):
            primes.append(last)
            yield last