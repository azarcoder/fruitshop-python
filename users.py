from fruits import *
import inquirer
import csv
from fpdf import FPDF

total_price = 0




def buy_fruit(fruitname, bought_fruits):
    global total_price
    fruit = list(filter(lambda f: f["fruitName"] == fruitname, Fruits.all_fruits))
    price = int(fruit[0]["price"])
    print(f"{fruitname} today price, RS:{price}")
    unit = fruit[0]["unit"]
    kg = int(input(f"Enter how many {unit}? "))
    total_price += price * kg
    bought_fruits.append(
        {
            "fruit": f"{fruitname}",
            # f"{unit}": kg,
            "kg" : kg,
            "unit": unit,
            "price": price,
            "total": price * kg,
        }
    )


#csv
def generate_bill(fruits_bought, total_amount):
    name = input("Customer name: ")
    with open(name + ".csv", "w", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=["fruit","kg", "unit", "price", "total"]
        )
        w.writeheader()
        for i in fruits_bought:
            w.writerow(i)
    print("Bill generated! Thank you for shopping with us :)")

#pdf
def generate_pdf_bill(bought_fruits, total_amount, customer_name="Customer"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, txt="Fruit Shop Bill", ln=True, align='C')
    pdf.ln(10)

    # Customer details
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Customer Name: {customer_name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Total Amount: Rs.{total_amount}", ln=True, align='L')
    pdf.ln(10)

    # Table header
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(50, 10, "Fruit", 1, 0, 'C')
    pdf.cell(30, 10, "Quantity", 1, 0, 'C')
    pdf.cell(30, 10, "Unit", 1, 0, 'C')
    pdf.cell(30, 10, "Price", 1, 0, 'C')
    pdf.cell(30, 10, "Total", 1, 1, 'C')

    # Table rows
    pdf.set_font("Arial", size=12)
    for fruit in bought_fruits:
        pdf.cell(50, 10, fruit['fruit'], 1, 0, 'C')
        pdf.cell(30, 10, str(fruit['kg']), 1, 0, 'C')
        pdf.cell(30, 10, fruit['unit'], 1, 0, 'C')
        pdf.cell(30, 10, str(fruit['price']), 1, 0, 'C')
        pdf.cell(30, 10, str(fruit['total']), 1, 1, 'C')

    # Save the PDF
    pdf_file_name = f"{customer_name}_bill.pdf"
    pdf.output(pdf_file_name)
    print(f"PDF bill generated: {pdf_file_name}")



while True:
    questions = [
        inquirer.List(
            "got",
            message="How can I help you?",
            choices=[
                "Watch all fruits",
                "View available fruits",
                "Watch fruits by price",
                "Imported fruits",
                "Buy fruits",
            ],
        ),
    ]
    answers = inquirer.prompt(questions)

    if answers["got"] == "Watch all fruits":
        Fruits.view_all_fruits()
    elif answers["got"] == "View available fruits":
        Fruits.available_fruits()
    elif answers["got"] == "Watch fruits by price":
        Fruits.price_range(int(input("minimum? ")), int(input("maximum? ")))
    elif answers["got"] == "Imported fruits":
        Fruits.search_by_import(input("Area: "))
    elif answers["got"] == "Buy fruits":
        total_price = 0
        bought_fruits = []
        while True:
            fruits = [
                fruit["fruitName"]
                for fruit in Fruits.all_fruits
                if fruit["availability"]
            ]
            f = [
                inquirer.List(
                    "got", message="choose fruit?", choices=fruits + ["quit"]
                ),
            ]
            answers = inquirer.prompt(f)
            choosen_fruit = answers["got"]
            if choosen_fruit == "quit":
                print(f"Your bill amount is : Rs.{total_price}")
                for i in bought_fruits:
                    print(i)
                a = input("Are you proceed to pay? [y/n]: ")
                if a.lower() == "y":
                    # generate_bill(fruits_bought=bought_fruits, total_amount=total_price)
                    generate_pdf_bill(bought_fruits, total_price, customer_name= input('Name: '))

                else:
                    break
            else:
                # buy function
                buy_fruit(choosen_fruit, bought_fruits)
