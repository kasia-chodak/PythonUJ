example = [[],[4],(1,2),[3,4],(5,6,7)]

def counting(example):
    result = []
    for element in example:
        summed_element = 0
        for smaller_element in element:
            summed_element += smaller_element
        result.append(summed_element)
    return result

print(counting(example))