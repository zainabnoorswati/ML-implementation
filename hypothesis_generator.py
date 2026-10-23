import itertools

def generate_hypotheses(attributes):
    # Step 1: Create a list of options for each attribute (adding '?')
    options = []
    for attr_name, values in attributes.items():
        new_list = values + ['?']
        options.append(new_list)
    
    # Step 2: Generate all possible combinations using itertools
    all_combinations = list(itertools.product(*options))
    
    # Step 3: Add the empty hypothesis (∅)
    empty_hypothesis = tuple(['∅'] * len(attributes))
    all_combinations.append(empty_hypothesis)
    
    # Step 4: Return the final list
    return all_combinations

# --- TEST THE CODE ---
my_attributes = {
    'Sky': ['Sunny', 'Rainy'],
    'AirTemp': ['Warm', 'Cold']
}

result = generate_hypotheses(my_attributes)

print(f"Total hypotheses generated: {len(result)}\n")
for hyp in result:
    print(hyp)