def grade(score):   
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

def main():
    print("Starting grading...")
    score = int(input("Enter your score (0-100): "))
    
    if 0 <= score <= 100:
        grade(score)
    else:
        print("Invalid score. Please enter a number between 0 and 100.")
    
    print("Grading complete.")

main()