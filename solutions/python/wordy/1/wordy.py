SIMPLE_OPERATIONS = {"plus", "minus"}
COMPOSED_OPERATIONS = {"multiplied", "divided"}
def answer(question):
    """Parses and evaluates simple math word problems.
    Supports numbers, addition, subtraction, multiplication, and division.
    The evaluation is performed sequentially from left to right.
    
    Args:
        question: The math word problem string.
        
    Returns:
        result: The result of the mathematical operations.

    Raises:
        ValueError: If the question format is invalid or contains unknown operations.
    """
    clean_question = question.rstrip("?").strip()
    words = clean_question.split()
    if len(words) < 3 or words[0] != "What" or words[1] != "is":
        raise ValueError("syntax error")
    equation = words[2:]
    
    if not equation:
        raise ValueError("syntax error")

    # Try to get the first value(int) from question
    try:
        result = int(equation[0])
    except:
        raise ValueError("syntax error")
    
    equation_index = 1
    while equation_index < len(equation):
        operation = equation[equation_index]
        
        # Operation is a digit
        if operation.isdigit(): 
            raise ValueError("syntax error")

        # Word not in operations
        if  operation not in SIMPLE_OPERATIONS and operation not in COMPOSED_OPERATIONS:
            raise ValueError("unknown operation")

        # Skip "by" from equation
        if operation in COMPOSED_OPERATIONS:
            if equation_index+1 >= len(equation) or equation[equation_index+1] != "by":
                raise ValueError("syntax error")
            equation_index+=1
            
        # Out of index
        if equation_index+1 >= len(equation): 
            raise ValueError("syntax error")
            
        # Try to get the second value(int) from question
        try: 
            next_number = int(equation[equation_index+1])
        except:
            raise ValueError("syntax error")

        if operation == "plus": # Addition
            result += next_number
            
        elif operation == "minus": #Subtraction
            result -= next_number
            
        elif operation == "multiplied": #Multiplication
            result *= next_number
        elif operation == "divided": # Divided
            if next_number == 0:
                raise ValueError("syntax error")
            result //= next_number
        else:
            raise ValueError("unknown operation")
        equation_index += 2
    return result
        
        
    
