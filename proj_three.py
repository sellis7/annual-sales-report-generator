#S Shaelyn Ellis - ITP100-HY1
#Proj03 - Annual Sales Report

def main():

    sales_file = open('SalesData.txt', 'r')  #open file to read
    sales_data = {} #make empty dictionary; used to sort names & sales, in tandem (extra credit)
    employees = []  #empty list for employees
    yrly_sales = [] #empty list for emp's tallied sales
    ttl_sales = 0.0 #accumulator for all sales
    ttl_comm = 0.0  #accumulator for all commissions
    ttl_bonus = 0.0 #accumulator for all bonuses
    print(' *Employee* \t\t  *Sales*   *Commiss.*   *Bonus*')  #header
    emp_name = sales_file.readline() #read first line of file as a declared variable
    while emp_name != '':            #while established variable is not a ''
        emp_name = emp_name.rstrip('\n') #strip endline from variable
        total = 0.0                #accumulator for totaling sales
        for entry in range(1, 13): #iterate through 12 entries/emp
            sales = float(sales_file.readline())#read next line of data
            entry += 1           #cycle through every name(stepped entry) for sales
            total += sales       #total sales for each emp
        sales_data[emp_name] = float(format(total, '.2f'))#DICTIONARY! EXTRA CREDIT
        emp_name = sales_file.readline()  #continue reading file
    sales_file.close()                #close file
    for key in sorted(sales_data):    #reorders content alphabetically by key(emp's names) & iterates
        firstLast = reorder_name(key) #now reorder the names first & last
        employees.append(firstLast)   #place ordered & sorted names in list
        yrly_sales.append(float(format(sales_data[key], '.2f')))#match sales data with names into a list
        comm = calc_comm(sales_data[key])  #calculate commission/emp's total sales
        bns = calc_bns(sales_data[key])    #calculate bonuses/emp's total sales
        show_data(firstLast, sales_data[key], comm, bns) #print statement of results
        ttl_sales += sales_data[key]  #total all sales while iterating
        ttl_comm += comm              #total all commissions while iterating
        ttl_bonus += bns              #total all bonuses while iterating
    show_ttls(ttl_sales, ttl_comm, ttl_bonus) #print statement totals
    avg_sales(employees, ttl_sales)           #calc & print average
    calcXtremes(employees, yrly_sales)        #calc & print min & max of yrly_sales list

def reorder_name(key):
    key = key.split(', ')   #establish each name(key) as a list to split
    firstLast = key[1] + ' ' + key[0]  #reorder names - first, last
    return firstLast

def calc_comm(total):      #if-elif-else statement to determine & calc commission
    if total >= 7000.00:
        comm = total * .0625
    elif total < 7000.00 and total >= 5000.00:
        comm = total * .04
    elif total < 5000.00 and total >= 3000.00:
        comm = total * .025
    else:
        comm = total * .015
    return comm

def calc_bns(total):    #if-else statements to determine & calc bonus
    if total >= 5000.00:
        bns = total * .0375
        return bns
    else:
        bns = 0.0
        return bns

def show_data(name, sales, comm, bns):  #present all lists & calculations
    print(name,'      \t', format(sales, ',.2f'), format(comm, '10.2f'), end='')
    if bns == 0.0:                  #if-else statement to present bonus result
        print('\tNo Bonus')
    else:
        print('\t', format(bns, '3.2f'))

def show_ttls(salesTl, commTl, bnsTl):  #print statement of all tallied figures
    print('--------------' *4)
    print('Annual Totals\t', format(salesTl, '16,.2f'), \
          format(commTl, '10,.2f'), format(bnsTl, '10,.2f'))

def avg_sales(emps, salesTl):   #calculate & print average based on # of emps
    salesAvg = salesTl / len(emps)
    print('\nAvg. Annual Sales/Emp:\t', format(salesAvg, ',.2f'))

def calcXtremes(emps, emp_sales):  #calculate & print min & max sales
    index = 0
    while index < len(emps):       #determine min & max while iterating through emps
        loIn = emp_sales.index(min(emp_sales))  #locate index of min
        hiIn = emp_sales.index(max(emp_sales))  #locate index of max
        index += 1
    print('\nWith $', format(emp_sales[loIn], ',.2f'), ', ', emps[loIn], \
          ' had the lowest annual sales.', sep='')
    print('With $', format(emp_sales[hiIn], ',.2f'), ', ', emps[hiIn], \
          ' had the highest annual sales.', sep='')

main()
