import math

# --- STEP 1: The Math Functions ---
def calculate_entropy(labels):
    total = len(labels)
    if total == 0: return 0
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def calculate_information_gain(data, target_col, attr_col):
    parent_labels = [row[target_col] for row in data]
    parent_entropy = calculate_entropy(parent_labels)
    
    unique_vals = set(row[attr_col] for row in data)
    weighted_child_entropy = 0
    
    for val in unique_vals:
        subset = [row for row in data if row[attr_col] == val]
        subset_labels = [row[target_col] for row in subset]
        subset_entropy = calculate_entropy(subset_labels)
        weighted_child_entropy += (len(subset) / len(data)) * subset_entropy
        
    return parent_entropy - weighted_child_entropy

# --- STEP 2: The Tree Builder ---
def build_tree(data, attributes, target_col):
    labels = [row[target_col] for row in data]
    
    # Base Case 1: Pure node
    if len(set(labels)) == 1:
        return labels[0]
    
    # Base Case 2: No attributes left
    if len(attributes) == 0:
        return max(set(labels), key=labels.count)
    
    # Find best attribute
    best_attr = None
    best_ig = -1
    for attr in attributes:
        ig = calculate_information_gain(data, target_col, attr)
        if ig > best_ig:
            best_ig = ig
            best_attr = attr
            
    # Build the tree structure
    tree = {best_attr: {}}
    unique_vals = set(row[best_attr] for row in data)
    remaining_attrs = [a for a in attributes if a != best_attr]
    
    for val in unique_vals:
        subset = [row for row in data if row[best_attr] == val]
        subtree = build_tree(subset, remaining_attrs, target_col)
        tree[best_attr][val] = subtree
        
    return tree

# --- STEP 3: Run the Code ---
# Our dataset (using the small 6-row example from our practice)
data = [
    {'Outlook': 'Sunny', 'Wind': 'Strong', 'Play': 'No'},
    {'Outlook': 'Sunny', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Outlook': 'Sunny', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Wind': 'Strong', 'Play': 'No'},
    {'Outlook': 'Rain', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Wind': 'Strong', 'Play': 'No'}
]

attributes = ['Outlook', 'Wind']

print("--- Building ID3 Tree ---")
final_tree = build_tree(data, attributes, 'Play')

import pprint
print("\nThe Tree Structure:")
pprint.pprint(final_tree)