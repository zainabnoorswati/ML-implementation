# Decision Tree Algorithms Comparison

This document compares the three main Decision Tree algorithms studied in class: **ID3**, **C4.5**, and **CART**. It outlines how they work, their mathematical differences, and why modern libraries prefer CART.

## 1. Algorithm Overviews

### ID3 (Iterative Dichotomiser 3)
Created by Ross Quinlan in 1986. It is the foundational decision tree algorithm. It builds the tree by choosing the attribute that provides the highest **Information Gain** (based on Entropy).
*   **Pros:** Easy to understand, interpretable.
*   **Cons:** Cannot handle continuous numbers, biased towards attributes with many unique values, and tends to overfit.

### C4.5 (Successor to ID3)
Also created by Ross Quinlan in 1993. It was designed to fix the flaws of ID3.
*   **Pros:** Uses **Gain Ratio** to fix the bias problem, handles continuous data (using thresholds), and uses pruning to prevent overfitting.
*   **Cons:** Can create complex multi-way splits, slower to compute.

### CART (Classification and Regression Trees)
Created by Leo Breiman in 1984. It is the industry standard and the algorithm used by Scikit-Learn.
*   **Pros:** Uses **Gini Impurity** (faster than logs), creates simple **binary splits**, and can perform both **Classification and Regression**.
*   **Cons:** Can be unstable (small data changes create different trees), but this is usually fixed using Random Forests.

---

## 2. Feature Comparison Table

| Feature | ID3 | C4.5 | CART |
| :--- | :--- | :--- | :--- |
| **Splitting Metric** | Information Gain | Gain Ratio | **Gini Impurity** (Class) / **Variance** (Reg) |
| **Split Type** | Multi-way | Multi-way | **Binary (Yes/No)** |
| **Task** | Classification | Classification | **Classification & Regression** |
| **Data Types** | Categorical only | Categorical + Continuous | Categorical + Continuous |
| **Overfitting Control** | None | Pruning | Pruning |
| **Handles Missing Values?** | No | Yes | Yes (surrogate splits) |

---

## 3. Why is CART considered the "Best" or Industry Standard?

Based on the implementations and the math, **CART** is the most robust choice for real-world applications for three reasons:

1.  **Speed:** Calculating Gini Impurity requires simple math (subtraction and squaring) compared to C4.5's Gain Ratio which requires complex logarithms. This makes CART much faster for large datasets.
2.  **Binary Splits:** CART always splits data into two branches (Yes/No). This creates a cleaner, more balanced tree structure compared to ID3 and C4.5 which can create hundreds of branches if an attribute has many values.
3.  **Versatility:** Only CART can handle Regression (predicting continuous numbers like house prices). 

*Note: While ID3 is great for learning the basics, and C4.5 is an excellent upgrade, CART is the algorithm that powers modern Machine Learning libraries (like `scikit-learn` and `XGBoost`).*