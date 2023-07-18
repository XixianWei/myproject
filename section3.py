# Section 3: Python Challenge [25 marks]
def calculate_classes(num_students):
    if not isinstance(num_students, int) or num_students <= 0:
        raise ValueError('Number of students should be a positive integer')

    # Number of classes can't be less than 2
    num_classes = max(2, (num_students + 29) // 30) 

    # Allocate students to classes as evenly as possible
    class_allocation = {f'Class {i+1}': num_students // num_classes for i in range(num_classes)}

    # Distribute the remaining students
    remainder = num_students % num_classes
    for i in range(remainder):
        class_allocation[f'Class {i+1}'] += 1

    print(f'Proposed Allocation: {num_classes} classes {class_allocation}')

# Testing the function
calculate_classes(31) 
calculate_classes(59)  
calculate_classes(87)  
calculate_classes(123)  
calculate_classes(21)  

