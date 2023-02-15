def validate(credits):

        try:
                credit_value = int(input(credits))

                if 0 <= credit_value <= 120 and credit_value % 20 == 0:

                        return credit_value

                else:
                        print("Out of Range.")

        except ValueError:

                print("Integer Required.")

        return validate(credits)                                             #return function validate to tackle the continuous invalid user input.



def verification():

        credit_pass = validate("Please Enter Your Credit at Pass: ")

        credit_defer = validate("Please Enter Your Credit at Defer: ")

        credit_fail = validate("Please Enter Your Credit at Fail: ")

        Total = credit_pass + credit_defer + credit_fail

        if Total != 120:

                print("Total Incorrect.")                                    #if the Total is incorrect prompt the user to input credit values back again
                                                                             #from the beginning.
                verification()                                               

        elif credit_pass == 120:

                print("Progress.")

        elif credit_pass == 100:                                             #progression outcome 'Progress(Module Trailer)' has two unique credit
                                                                             #value of '100' for 'Pass'.
                print("Progress(Module Trailer).")

        elif credit_pass + credit_defer >= 60:                               

                print("Do not Progress - Module Retriever.")

        else:
                print("Exclude.")

verification()                                                               #finally invoke the function 'verification' to start the program.



















        
