def process_form(name, email):
    return f"Thanks, {name}! Your email ({email}) has been received."

if __name__ == "__main__":
    name = "Natasha"
    email = "natasha.aidomon@gmail.com"
    message = process_form(name, email)
    print(message)