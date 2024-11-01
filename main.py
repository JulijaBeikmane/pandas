from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
money_machine.report()
coffee_maker = CoffeeMaker()
coffee_maker.report()

menu = Menu()

ieslegts = True

while ieslegts:
    iespejas = menu.get_items()
    izvele = input(f"Ko tu vēlies? ({iespejas})")
    if izvele == "off":
        ieslegts = False
    elif izvele == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        dzeriens = menu.find_drink(izvele)
        if coffee_maker.is_resource_sufficient(dzeriens) and (money_machine.make_payment(dzeriens.cost)):
            coffee_maker.make_coffee(dzeriens)

         
        # print(coffee_maker.is_resource_sufficient(dzeriens))
        
