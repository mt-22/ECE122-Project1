###############################
# Team members- Please enter your names here
# Name1: Marshall Taylor
# Name2: Ivan Li
###############################


def display_menu():
    """Display the list of polynomial available tools"""
    print("1-Insert; 2-Remove; 3-Info; 4-Evaluate; 5-Scaling; 6-Derive; 7-Integrate")
    print("8-Summation; 9-Subtract; 10-Multiply; 11-Divide")

def display_list(list_poly):
    for i in range(len(list_poly)): # iterate through the indexes of list_poly
        print(f"{i+1}: {get_expression(list_poly[i])}") # print each polynomial, labeling with index+1 to start at 1, rather than 0

def get_expression(arr):
    resp = '' 
    for i in range(len(arr)):
        if arr[i] != 0: # check value at index i
            if i == 0: resp += str(arr[i]) # if coefficient is multiplied by x^0, add only the coefficient to the response string
            elif i == 1: # check if the coeffficient is multiplied by x^1
                if arr[i] > 0: resp += f"+{arr[i]}x" #check if the coefficient is negative, adding a '+' sign prefix if not
                else: resp += f"{arr[i]}x"
            else:
                if arr[i] > 0: resp += f"+{arr[i]}x^{i}"
                else: resp += f"{arr[i]}x^{i}"
        # i += 1
    if not resp: return '0.0' # if there is nothing within the response string, return 0.0
    if resp[:1] == '+': resp = resp[1:] # if the response string begins with a '+' sign, remove it
    return resp
    # nice 2 liner but does not differentiate negative numbers or x^0/x^1
    # if all(x==0 for x in arr): return 0.0
    # return '+'.join(f"({c})x^{i}" for i,c in enumerate(arr) if c != 0)

def get_polynomial():
    deg = int(input('Degree of polynomial? '))
    resp = []
    for i in range(deg+1): # ask for deg+1 coefficients, so the degree is equal to the highest power
        num = input(f"Coefficient of x^{i}: ")
        if num == "": num = 0.0 # if no input given, set value to 0
        resp += [float(num)]
    return resp

def info(arr):
    even, odd, deg = 0, 0, 0 # initilizing variables
    for i in range(len(arr)): 
        if arr[i] != 0: # check value at index i
            if i%2 == 0: even += 1 #check if even
            else: odd += 1
            deg = i # set new degree if the value is non-zero
    if not even: return f"Degree is {deg} and it is odd"
    elif not odd: return f"Degree is {deg} and it is even"
    else: return f"Degree is {deg}"
    
def evaluate(arr, val):
    resp = 0
    for i in range(len(arr)):
        resp += arr[i]*(val**i) # add the coefficient multiplied by val param to the i power to the total
    return resp
    # one liner given the ability to use the sum() method
    #return sum(arr[i]*(val**i) for i in range(len(arr)))

def scale(arr, scale):
    if scale == 0: return [0.0]
    return [x*scale for x in arr] # multiply every coefficient by the scale param
    

def derive(arr):
    for i in range(len(arr)):
        arr[i] = arr[i]*(i) # multiply the coefficient by the degree of x
        if arr[i] == -0: arr[i] = 0.0 # fix negative zeros
    return arr
    # one liner, but gives negative zeros
    # return [arr[i]*i for i in range(len(arr))]

def integrate(arr, lb, ub):
    tot = 0
    for i in range(len(arr)):
        tot += (arr[i]/(i+1))*(ub**(i+1))-(arr[i]/(i+1))*(lb**(i+1)) # add the integral of the value at index i
    return tot
    # one liner assuming the sum() method is allowed
    # return sum((arr[i]/(i+1))*(ub**(i+1))-(arr[i]/(i+1))*(lb**(i+1)) for i in range(len(arr)))

def add(p1, p2):
    resp = []
    if len(p1) >= len(p2): # find the list with greater length
        for i in range(len(p1)):
            if i > (len(p2)-1): return resp + p1[i:] # if there are no more values in list p2, add the rest of list p1
            resp += [p1[i] + p2[i]] # add the common factors together
    else:  # same thing with p2 as longer list
        for i in range(len(p2)):
            if i > (len(p1)-1): return resp + p2[i:]
            resp += ([p1[i] + p2[i]])
    while (len(resp)) > 0 and not resp[len(resp)-1]: # loop while the list hold a value and the last item is 0
        resp = resp[:-1] # remove the last item (zero)
    if not len(resp): return [0.0] # if the response list has no values, return [0.0] (done to pass tests)
    return resp

def subtract(p1, p2):
    resp = []
    if len(p1) >= len(p2): # same method as add() method
        for i in range(len(p1)):
            if i > (len(p2)-1): return resp + p1[i:]
            resp += [p1[i] - p2[i]] # subtract the common factors
    else: 
        for i in range(len(p2)):
            if i > (len(p1)-1): return resp + [x*-1 for x in p2][i:] # if there are no more values in p1, add the rest of the list p2 multiplied by -1  
            resp += ([p1[i] - p2[i]])
    while (len(resp)) > 0 and not resp[len(resp)-1]: # remove trialing zeros like done in add() method
        resp = resp[:-1]
    if not len(resp): return [0.0] # if the response list has no values, return [0.0] (done to pass tests)
    return resp

def multiply(p1, p2):
    resp = [0] * (len(p1) + len(p2) - 1) # initialize empty array with length of expexted result
    for i in range(len(p1)):
        for j in range(len(p2)): # multiply each term in list p1 by every term in p2
            resp[i+j] += p1[i] * p2[j] # add the product to the coefficient with correlating exponent
    while (len(resp)) > 0 and not resp[len(resp)-1]: # remove trailing zeros
        resp = resp[:-1]
    if not len(resp): return [0.0] # if the response list has no values, return [0.0] (done to pass tests)
    return resp