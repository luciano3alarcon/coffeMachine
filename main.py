from typing import List, Optional
from Menu import MENU, resources

"""Constants"""
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

def coffeeBePrepared(strChoice):
    """Function dient für Zubereitung des Kaffees"""
    intTobePreparedWater = MENU[strChoice]["ingredients"].get("water")
    intTobePreparedMilk = MENU[strChoice]["ingredients"].get("milk")
    if intTobePreparedMilk is None:
        intTobePreparedMilk = 0
    intTobePreparedCoffee = MENU[strChoice]["ingredients"].get("coffee")
    subtractFromResources(intTobePreparedWater, intTobePreparedMilk, intTobePreparedCoffee)
    return intTobePreparedWater, intTobePreparedMilk, intTobePreparedCoffee


def subtractFromResources(intTobePreparedWater, intTobePreparedMilk, intTobePreparedCoffee):
    """Funktion zieht Zutaten aus den Ressources"""
    intNewWater = int(resources["water"]) - intTobePreparedWater
    intNewMilk = int(resources["milk"]) - intTobePreparedMilk
    intNewCoffee = int(resources["coffee"]) - intTobePreparedCoffee

    resources.update({"water" : intNewWater })
    resources.update({"milk": intNewMilk })
    resources.update({"coffee": intNewCoffee })


def calculateCostInput(quarters, dimes, nickles, pennies):
    """Rechnet Geld Eingabe"""
    floatInputQuart = float(QUARTERS * quarters)
    floatInputNickles = float(NICKLES * nickles)
    floatInputDimes = float(DIMES * dimes)
    floatInputPennies = float(PENNIES * pennies)
    return floatInputQuart + floatInputNickles + floatInputDimes + floatInputPennies


def calculateChange(floatSumMoneyInput, floatTobePreparedPreis):
    """Rechnet Geldrückgabe"""
    return floatSumMoneyInput - floatTobePreparedPreis


def fuelStandCheck(strChoice):
    """Überprüf den Füllstand der Resources"""
    fuelStand = True
    intChoiceWater = MENU[strChoice]["ingredients"].get("water")
    intChoiceMilk = MENU[strChoice]["ingredients"].get("milk")
    if intChoiceMilk is None:
        intChoiceMilk = 0
    intChoiceCoffee = MENU[strChoice]["ingredients"].get("coffee")

    if intChoiceWater > int(resources["water"]):
        fuelStand = False
    elif intChoiceMilk > int(resources["milk"]):
        fuelStand = False
    elif intChoiceCoffee > int(resources["coffee"]):
        fuelStand = False
    else:
        return fuelStand
    return fuelStand


def coffeeMachine():
    booPowerOn = True
    while booPowerOn:
        booEnoughRessource = True
        while booEnoughRessource:
            strChoice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: welcher Kaffee möchte der Nutzer serviert bekommen?
            booFuelStandCheck = fuelStandCheck(strChoice)
            if strChoice == "report":
                print("Water: " + str(resources["water"]) + "ml")
                print("Milk: " + str(resources["milk"]) + "ml")
                print("Coffee: " + str(resources["coffee"]) + "ml")
                """Check Füllstand von Resources"""
            elif strChoice == "espresso" or strChoice == "latte" or strChoice == "cappuccino":
                # TODO: Print einen Report mit der Kaffeemaschine (KM) Befüllung.
                if booFuelStandCheck:
                    print("Please insert coins")
                    quarters = float(input("How many quarters? "))
                    dimes = float(input("How many dimes? "))
                    nickles = float(input("How many nickles? "))
                    pennies = float(input("How many pennies? "))
                    floatSumMoneyInput = round(calculateCostInput(quarters, dimes,nickles, pennies),2)
                    floatTobePreparedPreis = MENU[strChoice].get("cost")
                    floatChangeMoney = round(calculateChange(floatSumMoneyInput, floatTobePreparedPreis),2)
                    coffeeBePrepared(strChoice)
                    print(f"Here is ${floatChangeMoney} in change.")
                    print(f"Here is your {strChoice}. Enjoy!")
                else:
                    booEnoughRessource = False
                    print("Sorry there is not enough water.")

        strMaintenance = input("Shut down or Maintenance: ")
        if strMaintenance == "maintenance":
            print("Please check the fill level of the resources.")
        else:
            booPowerOn = False
            print("The machine shuts down.")


coffeeMachine()

# TODO: Turn on und Turn off die Maschine
# TODO: Nun wird das Geld entgegengenommmen: Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# TODO: Vergleich, ob es genug Geld eingeworfen wurde Input vs Kaffee-Preis, bei Bedarf Rückgeld geben.
# TODO: Nach der Ausgabe sollte die Tankenbefüllung geringer werden. Neuer Report ziehen.
# TODO: “Here is your XXXXXX . Enjoy!”.


