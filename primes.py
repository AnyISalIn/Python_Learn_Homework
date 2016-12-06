def count_prime(n):
    primes = []
    c = 0
    max_primes = []
    max_value = int(n**0.5)
    for x in range(3, n+1, 2):
        c += 1
        if c == max_value/2:
            max_primes = primes[:]
        if x < max_value or x < 10:
            for prime in primes:
                if not x % prime:
                    break
            else:
                primes.append(x)
        else:
            for i in max_primes:
                if not x % i:
                    break
            else:
                primes.append(x)
    if n > 2:
        primes.insert(0, 2)
        
    return len(primes)

print count_prime(1000000)
