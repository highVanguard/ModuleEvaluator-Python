"""PROGRESSION OUTCOME"""

counterPass = 0
counterProgressModule = 0   #counter set to 0 to be added onto when the program is run
counterExclude = 0
counterRetriever = 0

def main(counterPass, counterProgressModule, counterExclude, counterRetriever): #main function
    print("############################################################")
    print("\n")
    print("    |||||||||||||||||||| HELLO ||||||||||||||||||||\n")
    print("~~~~~Welcome to the progression outcome calculator~~~~~\n")
    print("This program is to determine what progression outcome for you as a student have recieved to know where you are at the end of the year.")
    print("We will need to know what credits you have recieved for each of the following...\n")
    print("PASS\nDEFER\nFAIL\n")                                                                  #text displaying what the program does
    
    credit = [0, 20, 40, 60, 80, 100, 120] #credit range set in list
    print("The credit range is :", credit) 
    pass_credit(credit, counterPass, counterProgressModule, counterExclude, counterRetriever)#goes to the pass function carrying global variables
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    
def pass_credit(credit, counterProgress, counterProgressModule, counterExclude, counterRetriever): #pass credit input function
    Pass = input("- Please input your credits at pass :") #asks user to input credits at pass
    while Pass != credit: #loops the input to define whether the input was correct value or out of range
        try:
            Pass = int(Pass) #converts the input to int
            if Pass in credit:
                print("-------------------------------------")
                print("You have", Pass, "credits at pass")    #displays user input
                print("-------------------------------------")
                break #stops the loop from being never-ending
            elif Pass not in credit:
                print("\n>>>SORRY THAT IS OUT OF RANGE, PLEASE TRY AGAIN<<<\n") #validation check (range error), loops user back to input
                print("The credit range is :", credit)
                Pass = input("- Please input your credits at pass :")
                continue #keeps the loop continuous to have multiple attempts until the user inputs correct data
            break #stops the loop
                
        except ValueError: #checks whether the data is correct value (not an integer)
            print("\n>>>SORRY THAT IS NOT AN INTEGER, PLEASE TRY AGAIN<<<\n") #validation check (value error), loops the user back to input
            print("The credit range is :", credit)  
            Pass = input("- Please input your credits at pass :")
            continue#keeps the loop continuous to have multiple attempts until the user inputs correct data
        break #stops the loop
        
    defer_credit(Pass, credit, counterProgress, counterProgressModule, counterExclude, counterRetriever) #goes to the defer function carrying the data from the pass input
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    
def defer_credit(Pass, credit, counterProgress, counterProgressModule, counterExclude, counterRetriever): #defer credit input function
    Defer = input("- Please input your credits at defer :") #asks user to input credits at defer
    while Defer != credit: #loops the input to define whether the input was correct value or out of range
        try:
            Defer = int(Defer) #converts the input to int
            if Defer in credit:
                print("-------------------------------------")
                print("You have", Defer, "credits at defer")  #displays user input
                print("-------------------------------------")
                break #stops the loop from being never-ending
            elif Defer not in credit:
                print("\n>>>SORRY THAT IS OUT OF RANGE, PLEASE TRY AGAIN<<<\n") #validation check (range error), loops user back to input
                print("The credit range is :", credit)
                Defer = input("- Please input your credits at defer :")
                continue #keeps the loop continuous to have multiple attempts until the user inputs correct data
            break #stops the loop
        
        except ValueError: #checks whether the data is correct value (not an integer)
            print("\n>>>SORRY THAT IS NOT AN INTEGER, PLEASE TRY AGAIN<<<\n") #validation check (value error), loops the user back to input
            print("The credit range is :", credit)  
            Defer = input("- Please input your credits at defer :")
            continue #keeps the loop continuous to have multiple attempts until the user inputs correct data
        break #stops the loop
        
    fail_credit(Pass, Defer, credit, counterProgress, counterProgressModule, counterExclude, counterRetriever) #goes to fail function, carrying the data from the pass and defer input
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def fail_credit(Pass, Defer, credit, counterProgress, counterProgressModule, counterExclude, counterRetriever): #fail input function 
    Fail = input("- Please input your credits at fail :") #asks user to input credits at fail
    while Fail != credit:  #loops the input to define whether the input was correct value or out of range
        try:
            Fail = int(Fail) #converts the input to int
            if Fail in credit:
                print("-------------------------------------")
                print("You have", Fail, "credits at fail")    #displays user input
                print("-------------------------------------")
                total(Pass, Defer, Fail, credit, counterProgress, counterProgressModule, counterExclude, counterRetriever) #goes to the total function to calculate if the total of all inputs = 120
            elif Fail not in credit:
                print("\n>>>SORRY THAT IS OUT OF RANGE, PLEASE TRY AGAIN<<<\n") #validation check (range error), loops user back to input
                print("The credit range is :", credit)
                Fail = input("- Please input your credits at fail :")
                continue #keeps the loop continuous to have multiple attempts until the user inputs correct data
            break
                
        except ValueError: #checks whether the data is correct value (not an integer)
            print("\n>>>SORRY THAT IS NOT AN INTEGER, PLEASE TRY AGAIN<<<\n") #validation check (value error), loops the user back to input
            print("The credit range is :", credit)  
            Fail = input("- Please input your credits at fail :")
            continue #keeps the loop continuous to have multiple attempts until the user inputs correct data
        break #stops the loop
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""                
def total(Pass, Defer, Fail, credit, counterProgress, counterProgressModule, counterExclude, counterRetriever): #total calculation function, carrying data from all inputs        
    print("Thank you for your inputs, We will now calculate your progression outcome...")
    print("\n")
    Sum = int(Pass) + int(Defer) + int(Fail) #calculation sum process
    if Sum != 120:
        print("////////////////////////////////////////////////////////////////////")
        print("!!! Sorry, your credits must equal to a total of 120, try again !!!") #validation check (total error), displays that all inputs don't = 120
        print("////////////////////////////////////////////////////////////////////")
        print("\n")
        pass_credit(credit, counterProgress, counterProgressModule, counterExclude, counterRetriever) #takes the user back to input from the start at pass credit
    else:
        calc_correct(Pass, Defer, Fail, credit, counterProgress, counterProgressModule, counterExclude, counterRetriever) #if the total = 120, goes to progression outcomes     
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    
def calc_correct(Pass, Defer, Fail, credit, counterProgress, counterProgressModule, counterExclude, counterRetriever):
    if Pass == 120:
        counterProgress = counterProgress + 1
        #progress = counterProgress
        print("YOU HAVE THE OUTCOME OF...")
        print("\n")
        print("-> Progress")
        print("\n")
    elif Pass == 100:
        counterProgressModule = counterProgressModule + 1
        #progressMT = counterProgressModule
        print("YOU HAVE THE OUTCOME OF...")
        print("\n")
        print("-> Progress - Module Trailer")
        print("\n")
    elif Pass <= 20 and Fail >= 80:
        counterExclude = counterExclude + 1
        #exclude = counterExclude
        print("YOU HAVE THE OUTCOME OF...")
        print("\n")
        print("-> EXCLUDE")
        print("\n")
    else:
        counterRetriever = counterRetriever + 1
        #DNP = counterRetriever
        print("YOU HAVE THE OUTCOME OF...")
        print("\n")
        print("-> DO NOT PROGRESS - Module Retriever")
        print("\n")

    print("****THANK YOU FOR YOUR SUBMISSION!!****\n")   
    print("Please enter [Y] to enter new credits.")
    print("Otherwise enter [N] if you'd like to exit.")
    print("Alternatively if you are a member of staff and wish to see what outcomes students have been getting, please press [Q]\n")
    yes = ["Y", "y"]
    no = ["N", "n"]
    q = ["Q", "q"]
    try_again = input("Y / N / Q ?")
    while try_again != yes and no and q:
        if try_again in yes:
            main(counterProgress, counterProgressModule, counterExclude, counterRetriever)
        elif try_again in no:
            print("\n")
            print("Thank you for using this program, take care!")
            exit()
        elif try_again in q:
            progress = counterProgress
            progressMT = counterProgressModule
            exclude = counterExclude
            DNP = counterRetriever
            histogram(progress, progressMT, exclude, DNP)
        elif try_again not in yes and no and q:
            print(">>>SORRY THAT IS AN INCORRECT INPUT, PLEASE TRY AGAIN<<<")
            print("\n")
            try_again = input("Y / N / Q ?")
            continue
        break
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    
def histogram(progress, progressMT, exclude, DNP):
    print("\n")
    print("    ############### HISTOGRAM ###############    ")
    print("\n")
    star = "*"
    for x in star: #for loop to multiply the star by the numbers that are assigned into each variable
        print("STUDENT - PROGRESS ", progress, ":", star * progress, "\n")
        print("STUDENT - PROGRESS(MODULE TRAILER)", progressMT, ":", star * progressMT, "\n")   #prints the tally for each outcome
        print("STUDENT - DO NOT PROGRESS(MODULE RETREIEVER)", DNP, ":", star * DNP, "\n")
        print("STUDENT - EXCLUDE ", exclude, ":", star * exclude, "\n")
        
    print("\n")
    overall = progress + progressMT + exclude + DNP #adds total outcome
    print("OVERALL PROGRESSIONS :", overall) #prints total outcome

                
main(counterPass, counterProgressModule, counterExclude, counterRetriever)
    
    
