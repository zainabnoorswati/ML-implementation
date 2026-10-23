def does_it_cover(hypothesis, example):
    for h_val, e_val in zip(hypothesis, example):
        if h_val == '∅':
            return False
        if h_val != '?' and h_val != e_val:
            return False
    return True

def is_consistent(hypothesis, example, actual_label):
    prediction = 1 if does_it_cover(hypothesis, example) else 0
    return prediction == actual_label

# --- TEST THE CODE ---
print("--- Testing Consistency Checker ---")

# Test 1: Rule matches the example, and label is 1
rule1 = ('Sunny', 'Warm')
example1 = ('Sunny', 'Warm')
label1 = 1
print(f"Rule: {rule1}, Example: {example1}, Label: {label1} -> Result: {is_consistent(rule1, example1, label1)}")

# Test 2: Rule does NOT match the example, but label is 0 (Correct!)
rule2 = ('Sunny', 'Warm')
example2 = ('Rainy', 'Cold')
label2 = 0
print(f"Rule: {rule2}, Example: {example2}, Label: {label2} -> Result: {is_consistent(rule2, example2, label2)}")

# Test 3: Rule does NOT match the example, but label is 1 (Incorrect!)
rule3 = ('Sunny', 'Warm')
example3 = ('Rainy', 'Cold')
label3 = 1
print(f"Rule: {rule3}, Example: {example3}, Label: {label3} -> Result: {is_consistent(rule3, example3, label3)}")