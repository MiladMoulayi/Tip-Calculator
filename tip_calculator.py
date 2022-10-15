def tip_calc():
    # Create variables for the cost of the bill, the number splitting the bill, and the tip
    cost = float(input('What is the cost of the bill? '))
    split = float(input('How many people are splitting the bill? '))
    tip = float(input('What is the percentage of the tip? '))
    # Calculate the total tip, assign to total_tip
    total_tip = cost * (tip * .01)
    # Calculate the sales tax
    sales_tax = cost * .1
    # Calculate the total including tip and tax
    total_including_tip_and_tax = cost + total_tip + sales_tax
    # Calculate the cost per person
    cost_per_person = total_including_tip_and_tax / split
    # Format these numbers to print out to two decimal places
    format_total = "{:.2f}".format(total_including_tip_and_tax)
    format_per_person = "{:.2f}".format(cost_per_person)
    # Print the total and price per person
    print (f'Total bill: ${format_total}')
    print (f'Each person should pay ${format_per_person}')

tip_calc()

    



