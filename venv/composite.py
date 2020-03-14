
from sets import Set

class Composite:
    """The composite has at least one and at most two elements. The first compulsory element is a prime number. The second is either null or a prime number or another composite."""

    def __init__(self, square_floor, mandatory_prime, linked_composite=None, optional_prime=None):
        self.square_floor = square_floor
        self.mandatory_prime = mandatory_prime
        self.linked_composite = linked_composite
        self.optional_prime = optional_prime
        self.initialize_composite()

    def initialize_composite( self ) :
        if( self.has_composite() ):
            self.composite_nonprime = self.mandatory_prime * self.linked_composite.composite_nonprime
            return
        if ( self.has_optional_prime() ):
            self.composite_nonprime = self.mandatory_prime * self.optional_prime
            return
        self.composite_nonprime = self.mandatory_prime ** 2

    def __str__(self):
        my_factors = self.get_factors()
        my_factors.sort()
        obj_string = "Composite for [" + str(self.composite_nonprime) + "] -- prime factor [" + str(self.mandatory_prime) + "] -- second factor [" + str(self.optional_prime) + "] -- square floor [" + str( self.square_floor ) + "] -- factors " + str( my_factors ) + " "
        link_str = "Linked composite is [" + str(self.linked_composite.composite_nonprime) + "]" if self.has_composite() else "No linked composite."
        return obj_string + link_str

    def has_composite(self):
        return self.linked_composite is not None

    def lacks_composite(self):
        return self.linked_composite is None

    def has_optional_prime(self):
        return self.optional_prime is not None

    def get_factors(self):
        prime_factors_set = Set()
        self.get_prime_factors( prime_factors_set )
        factors_set = Set()
        for prime_factor in prime_factors_set:
            prime_factor_multiple = prime_factor
            while( prime_factor_multiple <= self.square_floor ):
                if( self.composite_nonprime % prime_factor_multiple == 0 ):
                    factors_set.add( prime_factor_multiple )
                    factors_set.add( self.composite_nonprime / prime_factor_multiple )
                prime_factor_multiple += prime_factor

        factor_list = [ 1, self.composite_nonprime ]
        for natural in factors_set:
            factor_list.append( natural )
        return factor_list

    def get_prime_factors( self, factor_set ):
        factor_set.add( self.mandatory_prime )

        if( self.has_optional_prime() ):
            factor_set.add( self.optional_prime )
            return

        if ( self.lacks_composite() ):
            return

        self.linked_composite.get_prime_factors( factor_set )

