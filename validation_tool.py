def validate_user_data(name, email, phone):
    if not name.strip():
        return "Name cannot be empty"
    
    if "@" not in email or "." not in email:
        return "Invalid email address"
    
    if not phone.isdigit() or len(phone) != 10:
        return "Phone number must be 10 digits long"
    
    return "User data is valid"

name = input("Enter your full name: ")
email = input("Enter your email address: ")
phone = input("Enter your phone number: ")

result = validate_user_data(name, email, phone)

print(result)
