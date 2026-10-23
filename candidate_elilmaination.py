# --- Tool: Consistency Checker ---
def does_it_cover(hypothesis, example):
    for h_val, e_val in zip(hypothesis, example):
        if h_val == '∅':
            return False
        if h_val != '?' and h_val != e_val:
            return False
    return True

# --- Main Algorithm ---
def candidate_elimination(attributes, training_data):
    num_attrs = len(attributes)
    
    # Initialize S and G
    S = [tuple(['∅'] * num_attrs)]
    G = [tuple(['?'] * num_attrs)]
    
    for example, label in training_data:
        # Convert example to tuple for comparison
        example = tuple(example)
        
        if label == 1: # Positive Example
            # 1. Generalize S
            new_S = []
            for s in S:
                if does_it_cover(s, example):
                    new_S.append(s)
                else:
                    new_h = list(s)
                    for i in range(num_attrs):
                        if new_h[i] == '∅':
                            new_h[i] = example[i]
                        elif new_h[i] != '?' and new_h[i] != example[i]:
                            new_h[i] = '?'
                    new_S.append(tuple(new_h))
            S = new_S
            
            # 2. Remove from G anything that doesn't cover the example
            G = [g for g in G if does_it_cover(g, example)]
            
        else: # Negative Example
            # 1. Remove from S anything that covers the example
            S = [s for s in S if not does_it_cover(s, example)]
            
            # 2. Specialize G
            new_G = []
            for g in G:
                if does_it_cover(g, example):
                    # Create specializations for each '?'
                    for i in range(num_attrs):
                        if g[i] == '?':
                            # Replace '?' with all possible values except the negative one
                            for val in attributes[list(attributes.keys())[i]]:
                                if val != example[i]:
                                    new_g = list(g)
                                    new_g[i] = val
                                    new_G.append(tuple(new_g))
                else:
                    new_G.append(g)
            
            # Remove any G that is more specific than another in G
            # (For simplicity in this code, we just keep the new_G)
            G = list(set(new_G)) 
            
    return S, G

# --- TEST THE CODE ---
print("--- Testing Candidate Elimination ---")

my_attributes = {
    'Sky': ['Sunny', 'Rainy'],
    'AirTemp': ['Warm', 'Cold']
}

my_data = [
    (["Sunny", "Warm"], 1),
    (["Sunny", "Cold"], 1),
    (["Rainy", "Cold"], 0)
]

final_S, final_G = candidate_elimination(my_attributes, my_data)

print("\nFinal S (Specific Boundary):")
for s in final_S:
    print(s)

print("\nFinal G (General Boundary):")
for g in final_G:
    print(g)