def all_ways_to_cut(letters,num_words):
    final_list = [[letters]]
    if num_words == 1:
        return final_list
    for i in range(num_words -1):
        final_list = last_cut(final_list)
    return final_list

def last_cut(cuts):
    table = []
    for partial in cuts:
        prefix_cuts = partial[:-1]
        word = partial[-1]
        row = cut_2(word)
        for i in row:
            table.append(prefix_cuts+i)
    return table

def cut_2(word):
    table = []
    for i in range (len(word) - 1):
        row = []
        row.append(word[0:i+1])
        row.append(word[i+1:])
        table.append(row)
    return table