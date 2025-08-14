#1 Contact form with optional fields

def submit_form(name, email, phone=None):
    print("Contact Form Submission:")
    print("Name:", name)
    print("Email:", email)
    if phone:
        print("Phone:", phone)
    else:
        print("Phone: Not Provided")

submit_form("Alice", "alice@example.com")
submit_form("Bob", "bob@example.com", "9876543210")


#2 Shopping cart total with *args

def calculate_total(*prices):
    total = sum(prices)
    return total

print("Total 1:", calculate_total(100, 200, 50))
print("Total 2:", calculate_total(99.99, 149.50))


#3 Display book info with **kwargs

def book_info(**kwargs):
    print("Book Details:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

book_info(title="1984", author="George Orwell", price="$10.99")


#4 Multi-item billing

def print_bill(*items):
    total = sum(items)
    print("Items:", items)
    print("Total Amount:", total)

print_bill(250, 300, 100)


#5 Use settings handler

def save_settings(**options):
    print("User Settings Saved:")
    for key, value in options.items():
        print(f"{key}: {value}")

save_settings(theme="dark", language="English", notifications=True)
