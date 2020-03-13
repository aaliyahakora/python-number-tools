
class Factors:

    def __init__(self):
        self.something = "Something"

    def get_factors( self, n ) :

        factor_list = [ 1, n ]
        halfway_point = n/2 if n % 2 == 0 else (n-1)/2

        for possible_factor in range( 2, halfway_point + 1 ):
            if ( possible_factor in factor_list ):
                break
            if ( n % possible_factor != 0 ):
                continue
            factor_list.append( possible_factor )
            if ( possible_factor * possible_factor == n ):
                continue
            factor_list.append( n/possible_factor )

        return factor_list

'''
def is_perfect(p):
    factor_list = get_factors( p )
    factor_list.remove( p )
    return sum ( factor_list ) == p


MAX_PERFECT = 1000000
for natural in range ( 2, MAX_PERFECT):
    if ( is_perfect( natural )):
        print ( "%s is a perfect number") % natural
    if ( natural % 50000 == 0 ):
        print ("%s done - %s left to do") % ( natural, MAX_PERFECT - natural )

print( "We found all the perfect numbers right up to %s" ) % MAX_PERFECT
'''