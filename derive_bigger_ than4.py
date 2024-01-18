# Define the known relations
relations = {
    ("A", "B"): "greater than",
    ("B", "C"): "greater than"
}

def derive_relation(stimulus1, stimulus2):
    # If the relation is directly known, return it
    if (stimulus1, stimulus2) in relations:
        return relations[(stimulus1, stimulus2)]
    elif (stimulus2, stimulus1) in relations:
        return "less than" if relations[(stimulus2, stimulus1)] == "greater than" else "greater than"
    
    # If the relation can be derived through another stimulus, return the derived relation
    for other_stimulus in set(x[0] for x in relations.keys()).union(x[1] for x in relations.keys()):
        if (stimulus1, other_stimulus) in relations and (other_stimulus, stimulus2) in relations:
            if relations[(stimulus1, other_stimulus)] == relations[(other_stimulus, stimulus2)]:
                return derive_relation(stimulus1, other_stimulus)
            else:
                return "cannot be determined"
    
    # If the relation cannot be determined, return a message indicating this
    return "cannot be determined"

# Print the derived relations
print("Derived relation between 'A' and 'C':", derive_relation("A", "C"))
print("Derived relation between 'C' and 'A':", derive_relation("C", "A"))
print("Derived relation between 'B' and 'A':", derive_relation("B", "A"))
print("Derived relation between 'A' and 'A':", derive_relation("A", "A"))


