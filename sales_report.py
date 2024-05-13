"""Generate sales report showing total melons each salesperson sold."""

"""Refactor this to {salesperson_name: melons_sold
unpack the variables
print salesreport function"""

def get_melons_sold_by_salesperson(file_path):
    mels_by_sales = {}
    with open(file_path) as f:
        for line in f:
            line = line.rstrip()
            salesperson_name, total_dollars, melons_sold = line.split("|")
            if salesperson_name in mels_by_sales:
                mels_by_sales[salesperson_name] += int(melons_sold)
            else:
                mels_by_sales[salesperson_name] = int(melons_sold)
        return mels_by_sales

def print_sales_report(melons_sold_by_salesperson):
    for salesperson_name, melons_sold in melons_sold_by_salesperson.items():
        print(f'{salesperson_name} sold {melons_sold} melons')


print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))

# # create an empty list of sales peoples' names that have sold melons
# salespeople = []
# # create an empty list of the number of melons each sales person sold
# melons_sold = []

# # open the sales-report.txt file as and refer to it as "f"
# f = open('sales-report.txt')

# # iterate over every line in sales-report.txt
# for line in f:
#     # strip the whitespace to the right
#     line = line.rstrip()
#     # divide each line by the "|" sign to get individual sales entries
#     entries = line.split('|')
#     # automate the extraction of each entry as the first item of the file
#     salesperson = entries[0]
#     # convert the number of melons (third item) into a number
#     melons = int(entries[2])
#     # if a given sales person is in the sales people list already
#     # increment that number of melons they have sold
#     if salesperson in salespeople:
#         # find the position where the salesperson is
#         position = salespeople.index(salesperson)
#         # reference that position to index the num of melons sold
#         melons_sold[position] += melons
#     # otherwise add a given salesperson to the list as well as how many
#     # melons that given salesperson has sold    
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# # iterate over the entire list of sales people
# for i in range(len(salespeople)):
#     # repeatedly print the final num of each unique person and 
#     # how many melons that person has sold
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')