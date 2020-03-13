
from composite import Composite
from prime_factory import PrimeFactory
from composites import Composites
from factors import Factors
from sets import Set

NUMBER_CEILING = 300
composite_dict = Composites( NUMBER_CEILING )

'''
for compo_key in composite_dict.composite_dictionary:
    the_composite = composite_dict.composite_dictionary[ compo_key ]
    print( "The factors for composite %s are %s" ) % ( the_composite.composite_nonprime, the_composite.get_factors() )
'''

for compo_key in composite_dict.composite_dictionary:
    the_composite = composite_dict.composite_dictionary[ compo_key ]
    compo_factor_list = the_composite.get_factors()
    compo_factor_list.sort()
    simple_factor_list = Factors().get_factors( the_composite.composite_nonprime )
    simple_factor_list.sort()
    if( compo_factor_list == simple_factor_list ):
        continue
    print( "For %s factor lists %s and %s are not the same." ) % ( compo_key, compo_factor_list, simple_factor_list )
