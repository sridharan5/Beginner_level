import data

machine_state = True
user_flavor = input("What would you like? (espresso/latte/cappuccino): ").lower()
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
money = {
    'money': 0.0
}
while machine_state:
    def resources():
        """This function is show the machine resources"""
        print("Resources: ")
        for i in data.resources:
            print(f"    {i}: {data.resources[i]}")


    def compare(comp):
        """ This function is return whether the condition is true or not """
        if comp == 'espresso':
            if data.MENU[comp]['ingredients']['water'] <= data.resources['water'] and data.MENU[comp]['ingredients'][
                'coffee'] <= data.resources['coffee']:
                return True
            else:
                report_input = input("Can't proceed. Do you want to see the resource 'yes' to view?  ").lower
                if report_input == 'yes':
                    resources()
                    print("I don't have a that much of resources.")
                return False

        else:
            if data.MENU[comp]['ingredients']['water'] <= data.resources['water'] and data.MENU[comp]['ingredients'][
                'milk'] <= data.resources['milk'] and data.MENU[comp]['ingredients']['coffee'] <= data.resources[
                'coffee']:
                return True
            else:
                report_input = input("Can't proceed. Do you want to see the resource 'yes' to view").lower
                if report_input == 'yes':
                    resources()
                    print("I don't have a that much of resources.")
                return False


    def flavors(flavor):
        """"This function take a flavor as a input"""
        if compare(flavor):
            resources()
            print(f"    Money: {money['money']}")
            print(f"The total cost around : {data.MENU[flavor]['cost']}")
            us_quarters = int(input("quarters: "))
            us_dimes = int(input("dimes: "))
            us_nickles = int(input("nickles: "))
            us_pennies = int(input("pennies: "))
            user_answer = (quarters * us_quarters) + (dimes * us_dimes) + (nickles * us_nickles) + (
                    pennies * us_pennies)
            if data.MENU[flavor]['cost'] <= user_answer:
                if data.MENU[flavor]['cost'] < user_answer:
                    extra_money = float(user_answer - data.MENU[flavor]['cost'])
                    print(f"Here is your {extra_money} dollars in change")
                    if flavor == 'espresso':
                        data.resources['water'] = data.resources['water'] - data.MENU[flavor]['ingredients']['water']
                        data.resources['coffee'] = data.resources['coffee'] - data.MENU[flavor]['ingredients']['coffee']
                        money['money'] += data.MENU[flavor]['cost']
                        print("process complete.............. Enjoy your coffee ...")
                        resources()
                        print(f"    Money: {money['money']}")
                        make_coffee_again = input("Do you want to make another coffeee? type 'yes' to make or 'off' to "
                                                  "off the coffee machine: ").lower()
                        if make_coffee_again == 'yes':
                            new_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
                            flavors(new_input)
                        if make_coffee_again == 'off':
                            print("machine off...")
                            global machine_state
                            machine_state = False
                    else:
                        data.resources['water'] = data.resources['water'] - data.MENU[flavor]['ingredients']['water']
                        data.resources['milk'] = data.resources['milk'] - data.MENU[flavor]['ingredients']['milk']
                        data.resources['coffee'] = data.resources['coffee'] - data.MENU[flavor]['ingredients']['coffee']
                        money['money'] += data.MENU[flavor]['cost']
                        print("process complete.............. Enjoy your coffee ...")
                        resources()
                        print(f"    Money: {money['money']}")
                        make_coffee_again = input("Do you want to make another coffeee? type 'yes' to make or 'off' to "
                                                  "off the coffee machine: ")
                        if make_coffee_again == 'yes':
                            new_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
                            flavors(new_input)
                        elif make_coffee_again == 'off':
                            print("machine off...")
                            machine_state = False
            else:
                print("sorry that's not enough money . Money refunded .")
                print("machine off...")
                machine_state = False


    flavors(user_flavor)