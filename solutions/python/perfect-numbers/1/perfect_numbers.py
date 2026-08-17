def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    Args:
        number (int): A positive integer

    Returns:
        (str) : The classification of the input integer
    """
    if number < 1 or not isinstance(number, int):
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = 0
    for num in range(1,number):
        div = number % num
        if div == 0:
            aliquot_sum+=num
    # Perfect Category
    if aliquot_sum == number:
        return "perfect"
    # Abundant Category
    if aliquot_sum > number:
        return "abundant"
    # Deficient Category
    return "deficient"
    
            
        
        