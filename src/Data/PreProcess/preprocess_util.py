from collections import Counter

def mass_normalization(lst : list, mu_min, std_max, linear = False) -> list: # if linear -> linear_scaling else Z-score
    # second and third parameter is either for z_score or linear scaling
    if linear:
        return [linear_scaling(i, mu_min, std_max) for i in lst]

    else:
        return [z_score(i, mu_min, std_max) for i in lst]
        


def z_score(x, mu, std): # x, expected value , standard deviation
    return (x - mu) / std

def linear_scaling(x, min, max): # give value between (0,1)
    return (x - min) / (max - min)

def probability_by_occurance(sample : list, possible_value = None):
    if possible_value == None:
        return probability_by_occurance_without_universe(sample)
        
    elif type(possiblie_value) is not list:
        print("Possible Values is not list")
        
    else:
        return probability_by_occurance_without_universe(sample, possible_value)

    return #ERROR#

# Should be private
def probability_by_occurance_with_universe(sample : list, possible_value : list) -> float:
    # possible_value must be all values of universe
    sample_size = len(sample)
    probabilities = dict(Counter(sample))
    

    for value in possible_value:
        if value not in probabilities:
            probabilities[value] = 0

    for value in probabilities:
        probabilities[value] = probabilities[value] / sample_size

    return probabilities

# Should be private
def probability_by_occurance_without_universe(sample : list) -> float:
    sample_size = len(sample)
    probabilities = dict(Counter(sample))

    for value in probabilities:
        probabilities[value] = probabilities[value] / sample_size
    
    return probabilities