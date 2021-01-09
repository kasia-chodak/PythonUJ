example = [1, 2, 3, 4]

def odwracanie(example_list):
    final_list = example_list[::-1]  # wykorzystuję metodę "List slicing" [start:stop:step]; step wynosi -1
    return final_list


print(odwracanie(example))