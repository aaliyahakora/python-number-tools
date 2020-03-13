
from composite import Composite
from prime_factory import PrimeFactory

class Composites:
    """The Composites holds both a Tree and a Dictionary of Composite objects."""

    def __init__( self, ceiling ):
        self.composite_dictionary = dict()
        self.prime_factory = PrimeFactory( ceiling )
        for non_prime in self.prime_factory.get_non_primes():
            fabricated_composite = self.manufacture_nonprime_composite( non_prime )
            self.composite_dictionary[ non_prime ] = fabricated_composite
            print( str( fabricated_composite ) )

    def manufacture_nonprime_composite( self, the_nonprime ) :
        first_prime_factor = self.prime_factory.get_first_prime_factor( the_nonprime )
        second_factor = the_nonprime / first_prime_factor

        if ( first_prime_factor == second_factor ):
            return Composite( first_prime_factor )
        if( self.prime_factory.is_prime( second_factor ) ):
            return Composite( first_prime_factor, None, second_factor )

        return Composite( first_prime_factor, self.composite_dictionary[ second_factor ] )
