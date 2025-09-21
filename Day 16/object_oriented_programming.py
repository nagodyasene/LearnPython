from turtle import Turtle, Screen
from prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon Name",["Charmander", "Pikachu", "Squirtle"])
table.add_column("Type", ["Fire", "Electric", "Water"])
table.align["Pokemon Name"]= "r"
table.align["Type"] = "l"

print(table)