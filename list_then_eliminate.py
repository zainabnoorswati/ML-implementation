import itertools

# --- Tool 1: Hypothesis Generator ---
def make_all_hypotheses(attributes):
    options = []
    for values in attributes.values():
        options.append(values + ['?'])
    
    combinations = list(itertools.product(*options))
    combinations.append(tuple(['∅'] * len(attributes)))
    return combinations

# --- Tool 2: Consistency Checker ---
def does_it_cover(hypothesis, example):
    for h_val, e_val in zip(hypothesis, example):
        if h_val == '∅':
            return False
        if h_val != '?' and h_val != e_val:
            return False
    return True

# --- Main Algorithm ---
def list_then_eliminate(attributes, training_data):
    # Step 1: List all hypotheses
    version_space = make_all_hypotheses(attributes)
    
    # Step 2: Eliminate inconsistent hypotheses
    for example, label in training_data:
        new_version_space = []
        
        for h in version_space:
            prediction = 1 if does_it_cover(h, example) else 0
            
            if prediction == label:
                new_version_space.append(h)
                
        version_space = new_version_space
        
    return version_space

# --- TEST THE CODE ---
print("--- Testing List-Then-Eliminate ---")

my_attributes = {
    'Sky': ['Sunny', 'Rainy'],
    'AirTemp': ['Warm', 'Cold']
}

# Our training data: 1 positive, 1 negative
my_data = [
    (["Sunny", "Warm"], 1),
    (["Rainy", "Cold"], 0)
]

final_rules = list_then_eliminate(my_attributes, my_data)

print(f"Total consistent rules found: {len(final_rules)}")
for rule in final_rules:
    print(rule)