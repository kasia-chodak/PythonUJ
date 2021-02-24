sequence1 = ['a', 'b', 'a', 1, 10, 'a', 34.4, 't', 10, 'c', 'g']
sequence2 = ['tt', 2, 'a', 34, 1, 'b', 'b', 'd', 'g', 'f']


def get_intersection(sequence_a, sequence_b):
    sequence_intersection = []
    if len(sequence_a) <= len(sequence_b):
        for element in sequence_a:
            for i in range(len(sequence_b)):
                if element == sequence_b[i]:
                    sequence_intersection.append(element)
    else:
        for element in sequence_b:
            for i in range(len(sequence_a)):
                if element == sequence_a[i]:
                    sequence_intersection.append(element)
    return sequence_intersection


def delete_multiple(sequence):
    return list(set(sequence))


sequence_C = delete_multiple(get_intersection(sequence1, sequence2))
sequence_merged = delete_multiple(sequence1 + sequence2)
print(sequence_C, sequence_merged)
