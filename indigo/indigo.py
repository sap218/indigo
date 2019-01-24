#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:17:10 2019
@author: samanfa
"""
import os
from termcolor import colored
"""
grey
red
green
yellow
blue
magenta
cyan 
white
"""

def setup(to_do_list):
    path = os.path.dirname(__file__)+"/input/tasklist.txt" # directory
    path_file = open(path) # opening file original

    print(colored("In-di-going...","cyan"))

    for line in path_file:
        to_do_list.append(line.rstrip())
    path_file.close() # closing file
    open(path, 'w+').close() # deletes entries from file    
    
    return (path, to_do_list)

##################################################################

def helping():
    print(colored("View list:\t'view'\nAdd tasks:\t'add'\nDone task:\t'done'\nNeed help:\t'help'\nShut down:\t'n'","yellow"))

def viewing(to_do_list):
    if not to_do_list:
        print(colored("Nothing here at the moment...","grey"))
    else:
        print(colored("\nHere are your tasks:","green"))
        i = 0
        for item in to_do_list:
            print("%s:\t%s"% (i,item))
            i += 1  

##################################################################

def adding(decision, ans, to_do_list):
    while ans != "n":
        print(colored("\nNote: when you have finished entering tasks, type: 'n'","red"))
        ans = input("Please enter task:\t")
        to_do_list.append(ans)
    
    if to_do_list[0] == "n":
        print("I'm going to say goodbye because you obviously don't know how to run me properly...")
        decision = 'n'
    else:
        to_do_list.remove('n')
        viewing(to_do_list)
            
    return (decision, to_do_list)

def completing(decision, to_do_list):
    if not to_do_list:
        print("You can't complete a task if you don't have any here!")
        decision = 'n'
    else:
        number = input("Which task number did you complete?\t")
        
        try:
            to_do_list.pop(int(number))
        except (IndexError, ValueError):
            print(colored("R U OK","magenta"))
        
        if not to_do_list:
            print(colored("\nCOMPLETED!\n","blue"))
            decision = 'n'
        elif number == 'n':
            print(colored("Let's try that again...","magenta"))
        else:
            viewing(to_do_list)
    return (decision, to_do_list)

##################################################################
##################################################################

def main():
    print("Setting up system...")
    to_do_list = []
    path, to_do_list = setup(to_do_list)
    
    print("Set-up ready.\n")
    print(colored("I am Indigo.","cyan"))
    print("\nWelcome to your to-do list for the day.")
    
    helping()
    print("\nWhenever you are ready, let me know what the plan is...")
    
    if not to_do_list:
        print(colored("Nothing here at the moment...","grey"))
    else:
        print(colored("\nHere are your tasks:","green"))
        i = 0
        for item in to_do_list:
            print("%s:\t%s"% (i,item))
            i += 1  
    
##################################################################
    
    decision = ""
    while decision != 'n':
        decision = input(">>\t")
        
        ans = "" # for adding
        
        if decision == "help":
            helping()
        
        elif decision == "add":
            decision, to_do_list = adding(decision, ans, to_do_list)
        
        elif decision == "done":
            decision, to_do_list = completing(decision, to_do_list)
        
        elif decision == "view":
            viewing(to_do_list)
            
            
        elif decision == 'n':
            print(colored("THX FOR SAVING","magenta"))
            
        else:
            print(colored("R U OK","magenta"))
            
            
    with open(path, 'w') as f: # reopening for writing
        for item in to_do_list:
            f.write("%s\n" % (item)) # adding tasks
    f.close() # closing
                
if __name__ == "__main__":
    main()   
