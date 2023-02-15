credit_pass = int(input("Please Enter Your Credit at Pass: "))

credit_defer = int(input("Please Enter Your Credit at Defer: "))

credit_fail = int(input("Please Enter Your Credit at Fail: "))

if credit_pass == 120 and credit_defer == 0 and credit_fail == 0:

    print("Progress.") 
    
elif  credit_pass == 100 and credit_defer == 20 and credit_fail == 0:

    print("Progress(Module Trailer).")                                                #As the question only asks about using conditional statements
                                                                                      #I deliberately didn't use user defined functions in part 1 code. 
elif credit_pass == 100 and credit_defer == 0 and credit_fail == 20:                  #This code will give the same output as it's been shown in bold
                                                                                      #in the question.
    print("Progress(Module Trailer).")

elif credit_pass == 40 and credit_defer == 0 and credit_fail == 80:

    print("Exclude.")

elif credit_pass == 20 and credit_defer == 20 and credit_fail == 80:

    print("Exclude.")

elif credit_pass == 20 and credit_defer == 0 and credit_fail == 100:

    print("Exclude.")

elif credit_pass == 0 and credit_defer == 40 and credit_fail == 80:

    print("Exclude.")

elif credit_pass == 0 and credit_defer == 20 and credit_fail == 100:

    print("Exclude.")

elif credit_pass == 0 and credit_defer == 0 and credit_fail == 120:

    print("Exclude.")

else:
    print("Do not Progress - Module Retriver.")




















    

