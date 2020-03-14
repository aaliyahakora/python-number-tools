
from composite import Composite
from prime_factory import PrimeFactory

class Composites:
    """The Composites holds both a Tree and a Dictionary of Composite objects."""

    def __init__( self, ceiling ):
        self.composite_dictionary = dict()
        self.prime_factory = PrimeFactory( ceiling )
        self.square_floor = 1
        for non_prime in self.prime_factory.get_non_primes():
            self.square_floor = self.get_square_floor( self.square_floor, non_prime )
            fabricated_composite = self.manufacture_nonprime_composite( non_prime )
            self.composite_dictionary[ non_prime ] = fabricated_composite
#            print( str( fabricated_composite ) )

    def manufacture_nonprime_composite( self, the_nonprime ) :
        first_prime_factor = self.prime_factory.get_first_prime_factor( the_nonprime )
        second_factor = the_nonprime / first_prime_factor

        if ( first_prime_factor == second_factor ):
            return Composite( self.square_floor, first_prime_factor )
        if( self.prime_factory.is_prime( second_factor ) ):
            return Composite( self.square_floor, first_prime_factor, None, second_factor )

        return Composite( self.square_floor, first_prime_factor, self.composite_dictionary[ second_factor ] )

    def get_square_floor( self, current_square_floor, current_nonprime ):
        if( ( current_square_floor + 1 ) ** 2 > current_nonprime ):
            return current_square_floor
        return current_square_floor + 1