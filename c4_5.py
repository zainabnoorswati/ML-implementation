import math

# --- Base Math Functions ---
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

def calculate_information_gain(data, target_col, attribute_col):
    parent_labels = [row[target_col] for row in data]
    parent_entropy = calculate_entropy(parent_labels)
    
    unique_vals = set(row[attribute_col] for row in data)
    weighted_child_entropy = 0
    
    for val in unique_vals:
        subset = [row for row in data if row[attribute_col] == val]
        subset_labels = [row[target_col] for row in subset]
        subset_entropy = calculate_entropy(subset_labels)
        weighted_child_entropy += (len(subset) / len(data)) * subset_entropy
        
    return parent_entropy - weighted_child_entropy

# --- C4.5 Functions ---
def calculate_split_info(data, attribute_col):
    total = len(data)
    counts = {}
    for row in data:
        val = row[attribute_col]
        counts[val] = counts.get(val, 0) + 1
        
    split_info = 0
    for count in counts.values():
        p = count / total
        split_info -= p * math.log2(p)
    return split_info

def calculate_gain_ratio(data, target_col, attribute_col):
    info_gain = calculate_information_gain(data, target_col, attribute_col)
    split_info = calculate_split_info(data, attribute_col)
    if split_info == 0:
        return 0
    return info_gain / split_info

# --- TEST THE CODE ---
print("--- Testing C4.5 (Gain Ratio) ---")

# Tricky dataset: 'ID' is unique for every row. 
# ID3 will LOVE it. C4.5 will PENALIZE it.
my_data = [
    {'ID': '1', 'Wind': 'Strong', 'Play': 'No'},
    {'ID': '2', 'Wind': 'Weak', 'Play': 'Yes'},
    {'ID': '3', 'Wind': 'Weak', 'Play': 'Yes'},
    {'ID': '4', 'Wind': 'Strong', 'Play': 'No'},
    {'ID': '5', 'Wind': 'Weak', 'Play': 'Yes'},
    {'ID': '6', 'Wind': 'Strong', 'Play': 'No'}
]

print(f"ID3 Information Gain (ID):   {calculate_information_gain(my_data, 'Play', 'ID'):.3f}")
print(f"C4.5 Gain Ratio (ID):        {calculate_gain_ratio(my_data, 'Play', 'ID'):.3f}")
print("-" * 30)
print(f"ID3 Information Gain (Wind): {calculate_information_gain(my_data, 'Play', 'Wind'):.3f}")
print(f"C4.5 Gain Ratio (Wind):      {calculate_gain_ratio(my_data, 'Play', 'Wind'):.3f}")