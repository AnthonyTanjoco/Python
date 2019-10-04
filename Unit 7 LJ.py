'''
Unit 7 Learning Journal
Anthony Tanjoco
'''
# original dictionary
family_names = {
    "fam1": ["Erica", "Dawn", "Tanjoco"],
    "fam2": ["Moriah", "Elizabeth", "Tanjoco"],
    "fam3": ["Joseph", "Anthony", "Tanjoco"],
}


def invert_dic(d):  # invert_dic code from assignment
    inverse = dict()
    for key in d:
        val = d[key]
        for n in val:  # modification to traverse list
            if n not in inverse:
                inverse[n] = [key]
            else:
                inverse[n].append(key)
    return inverse


# printing original and inverted dictionaries
print("Original Dictionary")
print()
print(family_names)
print()
print("Inverted Dictionary")
print()
print(invert_dic(family_names))

