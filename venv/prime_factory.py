
class PrimeFactory:

    def __init__( self, ceiling ):
        self.sieve = [True] * ceiling
        self.primes = []
        self.non_primes = []
        for i in range(2, ceiling):
            if self.sieve[i]:
                self.primes.append(i)
            for j in range(i * i, ceiling, i):
                self.sieve[j] = False
        for k in range (2, ceiling):
            if self.sieve[k] == False:
                self.non_primes.append(k)

    def get_primes(self):
        return self.primes

    def get_non_primes(self):
        return self.non_primes

    def get_first_prime_factor(self, nonprime):
        for prime in self.primes:
            if( nonprime % prime == 0 ):
                return prime

        raise RuntimeError( "Expecting to find a prime factor for non-prime {}".format( nonprime ) )

    def is_prime( self, num_to_test ):
        return num_to_test in self.primes