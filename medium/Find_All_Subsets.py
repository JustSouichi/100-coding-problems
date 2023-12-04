def find_subsets(s):
    subsets = [[]]
    for elem in s:
        subsets += [curr + [elem] for curr in subsets]
    return subsets
