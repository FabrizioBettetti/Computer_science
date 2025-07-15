from partition import get_partitions
import time

#========================
# Transporting Space Cows
#========================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    
    cows = {}
    with open(filename) as f:
        for line in f:
            pair = line.split(',')
            cow_name = pair[0].strip()
            if cow_name in cows:
                continue
            weight = int(pair[1].strip())
            cows[cow_name] = weight
    return cows


def print_dictionary(dictionary):
    for key in dictionary:
        print(key + ':', dictionary[key])


def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    trips = []
    done = False
    cowsSorted = {k: v for k, v in sorted(cows.items(), key=lambda item: item[1], reverse=True)}
    while not done:
        trip = []
        trip_weight = 0
        cowsSortedCopy = cowsSorted.copy()
        for cow_name in cowsSortedCopy:
            if trip_weight + cowsSortedCopy[cow_name] <= limit:
                trip.append(cow_name)
                trip_weight += cowsSortedCopy[cow_name]
                del(cowsSorted[cow_name])
        if len(trip) > 0:
            trips.append(trip)
        elif len(trip) == 0 or len(cowsSorted) == 0:
            done = True
    return trips        


def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    for trips in get_partitions(cows):
        trip_weight_exceeded = False
        for trip in trips:
            trip_weight = 0
            for cow_name in trip:
                trip_weight += cows[cow_name]
            if trip_weight > limit:
                trip_weight_exceeded = True
                break
        if trip_weight_exceeded:
            continue
        return trips


def compare_cow_transport_algorithms():
    """
    Using the data from cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    
    cows = load_cows('cow_data.txt')
    
    start = time.time()
    trips = greedy_cow_transport(cows)
    end = time.time()
    print('Algorithm: Greedy')
    print('Number of trips:', len(trips))
    print('Trips:', trips)
    print('Elapsed time:', end - start, 's')
    
    start = time.time()
    trips = brute_force_cow_transport(cows)
    end = time.time()
    print('Algorithm: brute force')
    print('Number of trips:', len(trips))
    print('Trips:', trips)
    print('Elapsed time:', end - start, 's')
