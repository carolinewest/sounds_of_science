def multiply(list1, list2):
    """This function was made to multiply the indicies of two lists together and return a list of the results"""

    #Function that multiplies the indecies of two same length lists together and returns a list of the results
    if len(list1)!=len(list2):#Checks whether the lists are of same length
        raise TypeError(f"Failed Multiplication. Lengths of the lists are not equal!")
    else:
        #Makes a list of the multiplied indicies
        result = [list1[i]*list2[i] for i in range(len(list1))]

        #Returns resulting list
        return result
    
    