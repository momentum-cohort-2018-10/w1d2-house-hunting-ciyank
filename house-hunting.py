annual_salary = float (input('Enter you annual salary '))
portion_saved = float (input ('Enter the percent of your salary to save, as a decimal '))
total_cost = float (input('Enter the cost of your dream home '))
num_of_months = 0
portion_down_payment = total_cost*.25
current_savings = 0
r = .04

while current_savings < portion_down_payment:
    num_of_months += 1
    current_savings = current_savings + (current_savings*r/12) + ((annual_salary/12)*portion_saved)
print ('num of months ' + str(num_of_months))



