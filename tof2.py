# Define the initial context-specific functions (Cfunc) of the stimuli
Cfunc = {
    "snake": "fear",
    "woods": "neutral",
}

# Define the relation
relations = {
    ("woods", "snake"): "contains"
}

def transform_function(stimulus1, stimulus2, crel):
    # If there is a relation and the context matches, transfer the function
    if (stimulus1, stimulus2) in relations and relations[(stimulus1, stimulus2)] == crel:
        Cfunc[stimulus2] = Cfunc[stimulus1]

# The context (Crel) that someone tells you that the woods contains the snake
transform_function("woods", "snake", "contains")

# Print the updated functions
print(Cfunc)  # Should print {"snake": "fear", "woods": "fear"}
