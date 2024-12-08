from datetime import datetime

def calculate_age():
    try:
        # Get the birth date from user
        birth_date = input("Enter your birth date (DD/MM/YYYY): ")
        
        # Convert string to date object
        birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
        
        # Get current date
        current_date = datetime.now()
        
        # Calculate age
        age = current_date.year - birth_date.year
        
        # Check if birthday hasn't occurred this year
        if current_date.month < birth_date.month or \
           (current_date.month == birth_date.month and current_date.day < birth_date.day):
            age -= 1
            
        print(f"\nYour age is: {age} years")
        
        # Calculate days until next birthday
        next_birthday = datetime(current_date.year, birth_date.month, birth_date.day)
        if next_birthday < current_date:
            next_birthday = datetime(current_date.year + 1, birth_date.month, birth_date.day)
        
        days_to_birthday = (next_birthday - current_date).days
        print(f"Days until your next birthday: {days_to_birthday} days")
        
    except ValueError:
        print("Invalid date format! Please use DD/MM/YYYY format.")

if __name__ == "__main__":
    print("Welcome to Age Calculator!")
    calculate_age()
