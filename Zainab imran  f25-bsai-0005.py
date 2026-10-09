# ==========================================
# Q#1) Student Result Management System
# ==========================================

def calculate_student_result(marks_dict):
    total = sum(marks_dict.values())
    percentage = (total / 300) * 100
    if percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'
    return total, percentage, grade

students = []

# Demo input for 5 students
sample_data = [
    ("Amaima", "F25-bSAI-0004", {"Python": 85, "AI": 90, "Math": 88}),
    ("Ali", "F25-bSAI-0010", {"Python": 72, "AI": 68, "Math": 75}),
    ("Zainab", "F25-bSAI-0005", {"Python": 95, "AI": 92, "Math": 94}),
    ("Usman", "F25-bSAI-0022", {"Python": 55, "AI": 60, "Math": 58}),
    ("Sara", "F25-bSAI-0015", {"Python": 45, "AI": 50, "Math": 48})
]

for name, roll, marks in sample_data:
    tot, perc, grd = calculate_student_result(marks)
    students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": tot,
        "percentage": perc,
        "grade": grd
    })

print("--- ALL STUDENTS RESULTS ---")
highest_student = max(students, key=lambda x: x["percentage"])

with open("results.txt", "w") as f:
    for s in students:
        info = f"Name: {s['name']} | Roll: {s['roll']} | Total: {s['total']} | Percentage: {s['percentage']:.2f}% | Grade: {s['grade']}"
        print(info)
        f.write(info + "\n")

print(f"\nHighest Percentage: {highest_student['name']} with {highest_student['percentage']:.2f}%")


# ==========================================
# Q#2) Word Analysis
# ==========================================

def analyze_sentence(sentence):
    words = sentence.split()
    total_words = len(words)
    total_chars = len(sentence)
    
    clean_words = [w.strip(".,!?").lower() for w in words]
    longest = max(clean_words, key=len)
    shortest = min(clean_words, key=len)
    
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in sentence if char in vowels)
    
    unique_words = set(clean_words)
    sorted_words = sorted(list(unique_words))
    
    analysis = f"""--- WORD ANALYSIS ---
Sentence: {sentence}
Total Words: {total_words}
Total Characters: {total_chars}
Longest Word: {longest}
Shortest Word: {shortest}
Vowel Count: {vowel_count}
Unique Words: {unique_words}
Alphabetical Words: {sorted_words}
"""
    print(analysis)
    with open("word_analysis.txt", "w") as f:
        f.write(analysis)

analyze_sentence("Artificial Intelligence and Programming in Python is fun and exciting")


# ==========================================
# Q#3) Simple Shopping Program
# ==========================================

products = [
    {"name": "Laptop", "price": 85000, "qty": 1},
    {"name": "Mouse", "price": 1200, "qty": 2},
    {"name": "Keyboard", "price": 2500, "qty": 1},
    {"name": "Headphones", "price": 4000, "qty": 1},
    {"name": "USB Drive", "price": 1500, "qty": 3}
]

total_bill = 0
print("--- SHOPPING BILL ---")
for p in products:
    item_total = p["price"] * p["qty"]
    p["total_price"] = item_total
    total_bill += item_total
    print(f"{p['name']} - Qty: {p['qty']} x Rs.{p['price']} = Rs.{item_total}")

discount = 0
if total_bill > 10000:
    discount = total_bill * 0.10

final_bill = total_bill - discount
most_expensive = max(products, key=lambda x: x["price"])

bill_summary = f"""
Total Bill: Rs.{total_bill}
Discount (10%): Rs.{discount}
Final Bill: Rs.{final_bill}
Most Expensive Item: {most_expensive['name']} (Rs.{most_expensive['price']})
"""
print(bill_summary)

with open("bill.txt", "w") as f:
    f.write(bill_summary)


# ==========================================
# Q#4) Simple Calculator
# ==========================================

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Cannot divide by zero"
def modulus(a, b): return a % b

print("--- CALCULATOR TEST ---")
num1, num2 = 20, 5
print(f"20 + 5 = {add(num1, num2)}")
print(f"20 - 5 = {subtract(num1, num2)}")
print(f"20 * 5 = {multiply(num1, num2)}")
print(f"20 / 5 = {divide(num1, num2)}")


# ==========================================
# Q#5) Small Restaurant Order System
# ==========================================

menu = {
    1: {"item": "Burger", "price": 500},
    2: {"item": "Pizza", "price": 800},
    3: {"item": "Fries", "price": 250},
    4: {"item": "Drink", "price": 150}
}

orders = [
    (1, 2), # 2 Burgers
    (2, 1), # 1 Pizza
    (4, 2)  # 2 Drinks
]

grand_total = 0
receipt = "--- RESTAURANT RECEIPT ---\n"

for item_id, qty in orders:
    item_info = menu[item_id]
    cost = item_info["price"] * qty
    grand_total += cost
    receipt += f"{item_info['item']} x {qty} = Rs.{cost}\n"

receipt += f"Grand Total: Rs.{grand_total}\n"
print(receipt)

with open("orders.txt", "w") as f:
    f.write(receipt)