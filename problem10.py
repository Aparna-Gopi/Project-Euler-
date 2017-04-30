
not_prime = []
prime = []
for i in xrange(2, 2000000):
    if i not in not_prime:
        prime.append(i)
        for j in xrange(i*i, 2000000, i):
            not_prime.append(j)
print prime
