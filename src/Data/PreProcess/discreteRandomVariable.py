def expectedValue(x_list : list, x_prob : dict, decimal = 5, power = 1) -> float:
    # returns E[x**power]

    expected_value = 0
    set_x_list = set(x_list)

    for x in set_x_list:
        expected_value += (x**power) * x_prob[x]

    return round(expected_value, decimal)


def variance(x_list : list, x_prob : dict, decimal = 5) -> float:
    
    vari = expectedValue(x_list, x_prob, 5 , 2) - (expectedValue(x_list, x_prob, 5))**2

    return round(vari, decimal)


def standardDeviation(x_list : list, x_prob : dict, decimal = 5) -> float:
    return round((variance(x_list ,x_prob))**0.5, decimal)



if __name__ == "__main__":
    from random import shuffle

    xs = list(range(1,10))
    probs = [0.0199, 0.1945, 0.3832, 0.277, 0.1091, 0.0142, 0.0015,
             0.0004, 0.002]
    probs = {x : prob for x, prob in zip(xs,probs)}

    print(f"Expected Value : {expectedValue(xs,probs)}")
    print(f"Variance : {variance(xs,probs)}")
    print(f"Standard Deviation : {standardDeviation(xs,probs)}")
