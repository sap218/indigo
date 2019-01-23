#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:17:10 2019
@author: samanfa
"""
import os
from os import path

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

def main():
    print("Setting up system...")
    
    path = os.path.dirname(__file__)+"/input/tasklist.txt" # directory
    #idpath = os.path.dirname(__file__)+"/input/tasklist.txt" # directory
    #path = 'tasklist.txt' # original
    #path = open(idpath) # original 
    
    path_file = open(path) # opening file original

    print(colored("In-di-going...","cyan"))

    to_do_list = []
    for line in path_file:
        to_do_list.append(line.rstrip())
    path_file.close() # closing file
    open(path, 'w+').close() # deletes entries from file    
    
    print("Set-up ready.\n")
    print(colored("I am Indigo.","cyan"))
    print("\nWelcome to your to-do list for the day.")
    
    print("\nWhenever you are ready, let me know what the plan is...")
    print(colored("Add more tasks: 'add'\nCompleted some tasks: 'done'\nView list: 'view'\nShut down: 'n'","yellow"))
    
    decision = ""
    while decision != 'n':
        decision = input(">>\t")
        
        ans = ""
        if decision == "add":
            while ans != "n":
                print(colored("\nNote: when you have finished entering tasks, type: 'n'","red"))
                ans = input("Please enter task:\t")
                to_do_list.append(ans)
            
            if to_do_list[0] == "n":
                print("I'm going to say goodbye because you obviously don't know how to run me properly...")
                decision = 'n'
            else:
                to_do_list.remove('n')
                print(colored("\n\nHere are your tasks:","green"))
                i = 0
                for item in to_do_list:
                    print("%s:\t%s"% (i,item))
                    i += 1
        
        elif decision == "done":
            if not to_do_list:
                print("I'm going to say goodbye because you obviously don't know how to run me properly...")
                decision = 'n'
            else:
                number = input("Which task number did you complete?\t")
                
                try:
                    to_do_list.pop(int(number))
                except IndexError:
                    print(colored("R U OK","magenta"))
                
                if not to_do_list:
                    print(colored("\nCOMPLETED!\n","blue"))
                    decision = 'n'
                elif number == 'n':
                    print(colored("R U OK","magenta"))
                else:
                    print(colored("\n\nHere are your tasks:","green"))
                    i = 0
                    for item in to_do_list:
                        print("%s:\t%s"% (i,item))
                        i += 1
        
        elif decision == "view":
            if not to_do_list:
                print(colored("Nothing here at the moment...","grey"))
            else:
                print(colored("\n\nHere are your tasks:","green"))
                i = 0
                for item in to_do_list:
                    print("%s:\t%s"% (i,item))
                    i += 1        
        else:
            print(colored("THX FOR SAVING","magenta"))
            
        with open(path, 'w') as f: # reopening for writing
            for item in to_do_list:
                f.write("%s\n" % (item)) # adding tasks
        f.close() # closing
                
if __name__ == "__main__":
    main()   
