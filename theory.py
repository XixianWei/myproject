# 1.1 The deque module is part of which python library? 
# The deque module is part of the collections Python library.

# 1.2 What are 2 differences that distinguish a tree from a graph? 
# 1)Hierarchy 2)Cyclic vs. Acyclic

# 1.3 Give the definitions of time complexity and space complexity 
# Time Complexity: the amount of time an algorithm takes to complete its task as a function of the input size. 
# It helps us analyze how the algorithm's performance scales with larger inputs.
# Space Complexity: the amount of memory space an algorithm uses to complete its task as a function of the input size. 
# It helps us analyze how the algorithm's memory usage scales with larger inputs.

# 1.4 Describe the bubble sort algorithm and its complexity. What is guaranteed at the end of the first pass?
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 
# This process is repeated for each element in the list until the entire list is sorted. The complexity of bubble sort is O(n^2), 
# where n is the number of elements in the list. At the end of the first pass of bubble sort, the largest element is guaranteed to have moved to its correct position at the end of the list.

# 1.5 Explain what LIFO and FIFO are and how each works in practice with a named data structure
# 1) LIFO stands for Last-In-First-Out.
# it is a principle where the last element added to a data structure is the first one to be removed. 
# This is commonly seen in the stack data structure, where elements are pushed onto the stack and popped off in reverse order of their addition.
# 2) FIFO stands for First-In-First-Out.
# It is a principle where the first element added to a data structure is the first one to be removed. 
# This is seen in the queue data structure, where elements are enqueued at the back and dequeued from the front.

# 1.6 What is a Balanced Binary Tree and what would be the best root? Walkthrough how you search using this structure.
# A balanced binary tree is a binary tree in which the difference in height between the left and right subtrees of any node is at most 1.
# This ensures that the tree remains relatively balanced and prevents degeneration into a linked list-like structure.

# The best root for a balanced binary tree would be the median element from a sorted list of elements. 
# This helps maintain balance by evenly distributing the elements on both sides.

# This is how do you search using this structure:
# Start at the root.
# If the target value is smaller, move to the left subtree.
# If the target value is larger, move to the right subtree.
# Repeat this process until the target value is found or the current node is null.
# Due to the balanced nature of the tree, the search process narrows down quickly, leading to efficient searches with a time complexity of O(log n) on average, where n is the number of nodes in the tree.

