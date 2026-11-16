# College Library Desk Management System

# Taking details from the user
member_name = input("Enter member name: ")
age = int(input("Enter member age: "))
borrowed_books = int(input("Enter number of books borrowed: "))

student_input = input("Is the member a student? (yes/no): ")

# Float data type
fine_amount = float(input("Enter fine amount: "))

# Boolean variable
is_student = student_input.lower() == "yes"

# Asking about a new book
new_book = input("Is a new book issued? (yes/no): ")

# Assignment operator
if new_book.lower() == "yes":
    borrowed_books += 1

# Membership operator
name_contains_a = 'a' in member_name.lower()

# Identity and logical operators
eligible = (
    is_student is True
    and age > 17
    and borrowed_books < 5
)

# Displaying membership summary
print("\n========== LIBRARY MEMBERSHIP SUMMARY ==========")

print(f"\nMember Name: {member_name}")
print(f"Age: {age}")
print(f"Books Borrowed: {borrowed_books}")
print(f"Student Status: {is_student}")
print(f"Fine Amount: Rs. {fine_amount:.2f}")

print(f"\nName contains letter 'a': {name_contains_a}")

if eligible:
    print("Membership Status: Eligible")
else:
    print("Membership Status: Not Eligible")

print("\nThank you for using Library Desk!")