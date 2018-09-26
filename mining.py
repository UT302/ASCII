from sys import exit
import math
from random import randint
from textwrap import dedent
from os import system

res = {'coal': 10,'copper': 0,'tungsten': 0,'iron': 0,'silver': 0}

rates = list(res.keys())

def show_available_res():
    print("You can mine:")
    print("=" * 25)
    o = 1
    for x in res.keys():
        print(o,x,"[Rate =", rates.index(x) + int(1), "/ day]" )
        o += 1
    print("=" * 25)


def print_res_cargo():
    print("Your resources:")
    print("+" * 25)
    for resource, amount in res.items():
        if resource in res and amount != 0:
            print(resource, amount)
    print("+" * 25)


def extr_rates(ore,work): 
    worktime = []              
    for x in res.keys():
        worktime.append(x)
    extracted = int(work) // int(worktime.index(ore))
    res[ore] += extracted



def extr_amount(item):
    print("How many days you wanna mine", item,"?")
    days = input("> ")
    extr_rates(item,days)
    
    

def mining_choice():
    options = []
    print_res_cargo()
    show_available_res()


    print("What are you mining?")
    for x in res.keys():
        options.append(x)
    choice = input("> ")
    ore = options[int(choice) - int(1)]
    print ("You mining", ore)
    extr_amount(ore)


while True:
    system('clear')
    print_res_cargo()
    show_available_res()
    print("What do you wanna do?\n1.Mine\n2.Build")
    choice = input("> ")

    if choice == '1':
        system('clear')
        mining_choice()   

