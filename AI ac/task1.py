def classify_age_group(age):
    """
    Classifies a person into an age group based on their age.
    
    Parameters:
        age (int): The age of the person.
        
    Returns:
        str: The age group ("Child", "Teenager", "Young Adult", "Adult", "Senior Citizen").
    """
    # Check for valid age input
    if age < 0:
        return "Invalid age"
    # Age group classification
    if age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    elif age <= 35:
        return "Young Adult"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior Citizen"

age = int(input("Enter age: "))
print(classify_age_group(age))
