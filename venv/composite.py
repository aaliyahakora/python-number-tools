
from sets import Set

class Composite:
    """The composite has at least one and at most two elements. The first compulsory element is a prime number. The second is either null or a prime number or another composite."""

    def __init__(self, mandatory_prime, linked_composite=None, optional_prime=None):
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
        obj_string = "Composite for [" + str(self.composite_nonprime) + "] -- prime factor [" + str(self.mandatory_prime) + "] -- second factor [" + str(self.optional_prime) + "] "
        link_str = "Linked composite is [" + str(self.linked_composite.composite_nonprime) + "]" if self.has_composite() else "No linked composite."
        return obj_string + link_str

    def has_composite(self):
        return self.linked_composite is not None

    def lacks_composite(self):
        return self.linked_composite is None

    def has_optional_prime(self):
        return self.optional_prime is not None

    def get_factors(self):
        composite_tree_set = Set()
        self.populate_factors(composite_tree_set)
        composite_factors_set = Set()
        for natural in composite_tree_set:
            composite_factors_set.add(natural)
            composite_factors_set.add(self.composite_nonprime/natural)
        factor_list = []
        for natural in composite_factors_set:
            factor_list.append(natural)
        return factor_list

    def populate_factors( self, factor_set ):
        factor_set.add( self.composite_nonprime )
        factor_set.add( self.mandatory_prime )

        if( self.has_optional_prime() ):
            factor_set.add( self.optional_prime )
            return

        if ( self.lacks_composite() ):
            return

        self.linked_composite.populate_factors( factor_set )

