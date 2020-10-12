def menu():
    d={'triangular_poppet' : triangular_poppet_unit_price , 'spring_roll' : spring_roll_unit_price}
    return(d)

def add_stock():
    global d
    global triangular_poppet_in_stock , spring_roll_in_stock 
    print(d)
    add = input('Enter what thing you want to add')
    num = int(input(f'Enter how many {add} you want to add'))
    if add == ('triangular_poppet'):
        triangular_poppet_in_stock += num
        d['triangular_poppet'] = triangular_poppet_in_stock 
        return (d)
    elif add == 'spring_roll' :
        spring_roll_in_stock += num
        d['spring_roll'] = spring_roll_in_stock
        return (d)
    else:
        print('enter valid input ')

def MyBakeShop():
    y=(calculate_bill(order,amount))
    print(f'your bill is {y} Rs')
    return (y)

## this function calculates the bill
def calculate_bill(order,amount):
    if order == 'triangular_poppet':
        price =  triangular_poppet_unit_price* amount
    else:
        price = spring_roll_unit_price * amount
    return (price)

# this function manage the stock after sales
def show_stock():
    d = {'triangular_poppet' : triangular_poppet_in_stock , 'spring_roll' : spring_roll_in_stock}
    return (d)

def switch_stock():
        x = d[order]        # this minus the value of stock from user enter amount to manage it
        x -= amount
        if order == 'spring_roll':
            spring_roll_in_stock = x
            d['spring_roll'] = spring_roll_in_stock
            return (d)
        elif order == 'triangular_poppet':
            triangular_poppet_in_stock = x
            d['triangular_poppet'] = triangular_poppet_in_stock 
            return (d)

#****************For Employees******************
# this function calculate employee basic salary
def employee_salary():
    Chef_salary  = Chef_wage_rate * Chef_hrs
    Salesman_salary = Salesman_wage_rate * Salesman_hrs
    print('Chef salary is', Chef_salary)
    print('Salesman salary is ', Salesman_salary)
    return (Chef_salary , Salesman_salary)

# this function calculate the bonus of employee as per hour #
def employee_bonus():
    bonus_hr = 500
    chef_bonus_hr = int(input("Please, Enter extra working hours of Chef:"))
    if (chef_bonus_hr ) >= 0:
        chef_bonus = (bonus_hr * chef_bonus_hr)
        print('Chef bonus is', chef_bonus)
    Salesman_bon_hr = int(input("enter extra working hours of Salesman:"))
    if (Salesman_bon_hr) >= 0:
        Salesman_bonus = (bonus_hr * Salesman_bon_hr )
        print(' Salesman bonus is ', Salesman_bonus)
    return (chef_bonus , Salesman_bonus )

def extra_bonus(total_sales):
    if total_sales> 2500:
        extra_bonus = 250
        return (extra_bonus) 
    else:
        extra_bonus = 0
        print('Total sales < 2500 , so you won\'t get bonus')
        return (extra_bonus)
    
# This function calculate total salary
 
def MyEmployee():
        y = employee_salary()
        Chef_salary =  (y[0])
        Salesman_salary =  (y[1])
        z = employee_bonus()
        Chef_bonus =  (z[0])
        Salesman_bonus =  (z[1])
        extras = extra_bonus(total_sales)
        print ('extra bonus is allocate to both employees which is ', extras)
        total_1 = Chef_salary + Chef_bonus + extras
        print ('The total salary of Chef' , total_1)
        total_2 = Salesman_salary + Salesman_bonus + extras
        print ('The total salary of Salesman' ,total_2)

#### BOUTIQUE #############

def cloth_shop(visit):
    global total_sales
    if visit == 1:
        d={ 'frock' : 2000 , 'shirts' : 1500 , 'earings' : 500 , 'scarf' : 500 }
    elif visit == 2:
        d={ 'baby suits' : 2000 , 'baba suits' : 2500 , 'sandles' : 1250 , 'snickers' : 1500 }
    else:
        d={ 'pants' : 1700 , 'shirts' :1200 , 'neck tie' : 500 , 'watch' : 1500 }
    
    for i in d:
        print(i)
    choice = input('What do you want to buy')
    print('the price of ', choice , 'is' , d[choice])
    bill = input('Enter yes if you want to buy it ')
    if bill == 'yes':
        total_bill = d[choice]
        print(f'your bill is {total_bill}')
        total_sales += total_bill
    else:
        print ('checkout another things')
    return total_sales

def add_stock_2():
    global d2
    global  women_stock , men_stock , child_stock
    print(d2)
    add = input('Enter what thing you want to add')
    num = int(input(f'Enter how many {add} you want to add'))
    if add == 'women_stock' :
        women_stock += num
        d2[add] = women_stock
        return (d2)
    elif add == 'men_stock' :
        men_stock  += num
        d2[add] = men_stock
        return (d2)
    elif add == 'child_stock' :
        child_stock  += num
        d2[add] = child_stock 
        return (d2)

women_stock = 500
men_stock = 500
child_stock = 500

Chef_wage_rate = 300
Salesman_wage_rate = 350
Chef_hrs = 8
Salesman_hrs =10

triangular_poppet_in_stock = 500
spring_roll_in_stock = 500

triangular_poppet_unit_price = 25
spring_roll_unit_price = 30
total_sales = 0

d = {'triangular_poppet' : triangular_poppet_in_stock , 'spring_roll' : spring_roll_in_stock}
d2 = {'women_stock' : women_stock , 'men_stock' : men_stock , 'child_stock': child_stock}
order = None
while True:
    print('''         ****** WELCOME *******
	  1.  Sunshine Bakers
	  2.  New Verstile Bella Boutique
	  3.  Check Employee Salary
	  4.  Add Stock
	  5.  Check Manage Stock (first buy sth then instead goto 6)
	  6.  Show Stock
	  7.  Exit 
    Enter no. where you want to go''')
    try:
        x = int(input('>>> '))
        if x ==1:
            print(menu())
            order = input('Enter the name of snacks you want to buy\n>>>')
            order = order.lower()
            if order == 'no':
                print('Thanks for coming')
            else:
                amount = int(input(f'enter how many {order} you want to buy\n>>>'))
            sales = MyBakeShop()
            total_sales += sales
                
        if x == 2:
            visit = int(input('Enter \n 1 ==> for women_shop \n 2 ==> for child_closet \n 3 ==> for men_shop\n>>>'))
            sales2 = cloth_shop(visit)
            total_sales = sales2

        if x == 3:
            MyEmployee()

        if x== 4:
            enter = int(input('which stock you want to add \n 1=> bakery \n 2=> boutique\n>>'))
            if enter == 1:
                print (add_stock())
            elif enter ==2 :
                print(add_stock_2())
            else:
                print('valid entry please')

        if x == 5:
            if order == None:
                print(show_stock())
            else:
                print ('The remaining stock is here')
                print (switch_stock())

        if x == 6:
            print(show_stock())        

        if x == 7:
            print ('Your total bill is ' , total_sales)
            print ('~~~~~Thanks for coming~~~~~')
            break
    except ValueError:
        print ('please select correctly')
    
