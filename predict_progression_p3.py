Progress = 0
Trailing = 0
Retriever = 0                                                        #assigning an "initial value" of 0 to Progress, Trailing, Retriever & Excluded
Excluded = 0

def HorizontalHistogram():
    
    Outcome = Progress + Trailing + Retriever + Excluded
    
    print("Progress: ", Progress, Progress * "*")
    
    print("Trailing: ", Trailing, Trailing * "*")
    
    print("Retriever:", Retriever, Retriever * "*")
    
    print("Excluded: ", Excluded, Excluded * "*")
    
    if Outcome > 1:
        
        print("Total Outcomes are", Outcome)

    else:

        print("Total Outcome is", Outcome)
        




def validate(credits):

        try:
                credit_value = int(input(credits))

                if 0 <= credit_value <= 120 and credit_value % 20 == 0:

                        return credit_value

                else:
                        print("Out of Range.")

        except ValueError:

                print("Integer Required.")

        return validate(credits)





def verification():
    
        global Progress, Trailing, Retriever, Excluded

        credit_pass = validate("Please Enter Your Credit at Pass: ")

        credit_defer = validate("Please Enter Your Credit at Defer: ")

        credit_fail = validate("Please Enter Your Credit at Fail: ")

        Total = credit_pass + credit_defer + credit_fail

        if Total != 120:

                print("Total Incorrect.")                                   
                                                                             
                verification()                                               

        elif credit_pass == 120:

                print("Progress.")
                
                Progress = Progress + 1                                                   #counting how many times "Progress" is printed.

        elif credit_pass == 100:                                             
                                                                             
                print("Progress(Module Trailer).")

                Trailing = Trailing + 1                                                   #counting how many times "Progress(Module Trailer)" is printed.

        elif credit_pass + credit_defer >= 60:                               

                print("Do not Progress - Module Retriever.")

                Retriever = Retriever + 1                                                 #counting how many times "Do not Progress - Module Retriever" 
                                                                                          #is printed.
        else:
                print("Exclude.")

                Excluded = Excluded + 1                                                   #counting how many times "Excluded" is printed.                                           


def Decision():

    while 1 == 1:

        verification()

        Question = input("Would You Like to Enter Another Set of Data? \nPress Any Key to Proceed or 'q' to Quit & View Results: ")

        if Question.lower() == "q":

            HorizontalHistogram()

            break                                                                         #breaking the While loop.

Decision()                                                                                #finally invoking the function. :)























