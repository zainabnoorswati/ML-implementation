def find_s(training_data, num_attributes):
    # 1. Start with the most specific hypothesis (all ∅)
    h = ['∅'] * num_attributes
    
    # 2. Loop through every example
    for example, label in training_data:
        
        # 3. Only process Positive examples (label == 1)
        if label == 1:
            
            # We need a temporary list to hold the updated rule
            new_h = []
            
            # 4. zip() pairs the rule and the example together
            for h_val, e_val in zip(h, example):
                
                # 5. If h is ∅, replace with the example's value
                if h_val == "∅":
                    new_h.append(e_val)
                    
                # 6. If h doesn't match the example, generalize to '?'
                elif h_val != "?" and h_val != e_val:
                    new_h.append("?")
                    
                # 7. If they match, keep the value
                else:
                    new_h.append(h_val)
            
            # 8. Update our main hypothesis
            h = new_h
            
    # 9. Return the final rule
    return h

# --- TEST THE CODE ---
print("--- Testing Find-S Algorithm ---")

# Our dataset: 2 positive examples, 1 negative example
my_data = [
    (["Sunny", "Warm"], 1),
    (["Sunny", "Cold"], 1),
    (["Rainy", "Cold"], 0)
]

# We have 2 attributes (Sky and AirTemp)
final_rule = find_s(my_data, 2)
print("Final Hypothesis:", final_rule)