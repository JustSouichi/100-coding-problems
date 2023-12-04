def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        key = tuple(sorted(s))
        anagrams[key] = anagrams.get(key, []) + [s]
    return list(anagrams.values())
