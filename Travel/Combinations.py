from Travel import TravelCost, Location, Path

def log( line ):
    verbose = False
    if verbose:
        print("{}".format( line ))

class Combinations:

    @staticmethod
    def calcSinglePath( cities ):
        """ This is intended to calculate all paths
            between all cities passed in
        """
        if len(cities) == 1:
            return [ Path.Path(cities[0], cities[0]) ] 
        elif len(cities) == 2:
            result = [ Path.Path(cities[0], cities[1]), Path.Path(cities[1], cities[0]) ]
            return result

        # 3 cities
        #  pick 1 city as starting point
        print("DEBUG")
        for city in cities:
            print(f"Starting point {city}")
            remainingCities = sorted(set(cities) - set(city))
            print(f"Remaining cities: {', '.join(remainingCities)}")
        #

    @staticmethod
    def calc( guests ):
        """ This looks optimized for CarPool
            because it allows for people to drive alone
        """
        if len( guests ) == 1:
            allPaths = [ ]
            allPaths.append ([ (guests[0],)  ]) # A drives alone
            return allPaths
        elif len( guests ) == 2:
            gA = guests[0]
            gB = guests[1]
            allPaths = [ ]
            allPaths.append ([     ( gA, ), ( gB, )   ]) # A and B drive alone
            allPaths.append ([     ( gB, ), ( gA, )   ]) # B and A drive alone
            allPaths.append ([     ( ( gA,  gB ) )    ]) # A drives and picks up B
            allPaths.append ([     ( ( gB,  gA ) )    ]) # B drives and picks up A
            return allPaths
        else:
            allPaths = [ ]
            for guest in guests: # [ A, B, C, D ]
                # { A }, remaining-> { B, C, D }
                remaining = sorted(set(guests) - set(guest))
    
                for i in range( len(remaining)+1 ):
                    # Fix A picks 1
                    log( " {} picks {} guests".format( guest, i ))
    
                    if i == 0:
                        leftSet = (guest,)
                        remainingSet = set(remaining) - set(leftSet)
                        log("   left: {}, remaining: {} ".format( leftSet, remainingSet ))
                        if len(remainingSet) == 0:
                            leftSet = [ leftSet ]
                            log("ALL_PATHS.0a.append( {} )".format( leftSet ))
                            allPaths.append( leftSet )
                        elif len(remainingSet) == 1:
                            leftSet = [ leftSet, tuple(remainingSet) ]
                            log("ALL_PATHS.1a.append( {} )".format( leftSet ))
                            allPaths.append( leftSet )
                        else:
                            rightPaths = Combinations.calc( list(remainingSet) )
                            for rPath in rightPaths:
                                rPath.insert( 0, leftSet )
                                log("ALL_PATHS.2a.append( {} )".format( rPath ) )
                                allPaths.append( rPath )
                    else:
                        from itertools import combinations, permutations, product
                        subSet = permutations( remaining, i )
                        for left in subSet:
                            # A, left
                            leftSet = (guest,) + left
                            remainingSet = set(remaining) - set(leftSet)
                            log("   left: {}, remaining: {} ".format( leftSet, remainingSet ))
                            if len(remainingSet) == 0:
                                leftSet = [ leftSet ]
                                log("ALL_PATHS.0b.append( {} )".format( leftSet ))
                                allPaths.append( leftSet )
                            elif len(remainingSet) == 1:
                                leftSet = [ leftSet, tuple(remainingSet) ]
                                log("ALL_PATHS.1b.append( {} )".format( leftSet ))
                                allPaths.append( leftSet )
                            else:
                                rightPaths = Combinations.calc( list(remainingSet) )
                                log("ALL_PATHS_2: rightPaths={}".format( len(rightPaths) ))
                                for rPath in rightPaths:
                                    rPath.insert( 0, leftSet )
                                    log("ALL_PATHS.3b.append( {} )".format( rPath ) )
                                    allPaths.append( rPath )
            return allPaths

