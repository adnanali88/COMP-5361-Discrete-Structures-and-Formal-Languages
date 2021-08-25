#Globals
#Tautology boolean
Tautol = False
#Contingency boolean
Contin = False
#Contradiction boolean
Contra = False
#Count for the amount of variables i.e n count for P = [P1,P2,P3,...,Pn]
count = 0


def fix_array(Vars,logi):
    variable_array = Vars.split(',')
    logi = logi.replace('TRUE', 'T')
    logi = logi.replace('FALSE', 'F')
    return variable_array,logi

def logic_val(Vars_array,Vals_array,logi):
    varval = dict(zip(Vars_array,Vals_array))
    for P,V in varval.items():
        logi = logi.replace(P,V)
    return logi



def logic_eval(logi):
    
    #Evalute compliment
    #while '-' in logi:
    logi = logi.replace('- F', 'T')
    logi = logi.replace('- T', 'F')
    
    #Evaluate 'AND' and 'OR'
    #while 'AND' or 'OR' in logi:
    logi = logi.replace('T AND T', 'T')
    logi = logi.replace('F AND T', 'F')
    logi = logi.replace('T AND F', 'F')
    logi = logi.replace('F AND F', 'F')
        
    logi = logi.replace('F OR F', 'F')
    logi = logi.replace('F OR T', 'T')
    logi = logi.replace('T OR T', 'T')
    logi = logi.replace('T OR F', 'T')
       
        

    #Evaluate 'THEN'
    #while 'THEN' in logi:
    logi = logi.replace('T THEN F', 'F')
    logi = logi.replace('T THEN T', 'T')
    logi = logi.replace('F THEN F', 'T')
    logi = logi.replace('F THEN T', 'T')
        
    #Evaluate '='
    #while 'EQUALS' in logi:
    logi = logi.replace('T EQUALS T', 'T')
    logi = logi.replace('F EQUALS F', 'T')
    logi = logi.replace('T EQUALS F', 'F')
    logi = logi.replace('F EQUALS T', 'F')
    
    return logi

def bracket_eval(logi, start):
    try:
        i = logi.index('(', start)
        for x in range(i+1,len(logi)):
            if logi[x] == '(':
                return bracket_eval(logi,x)
            elif logi[x] == ')':
                return logi[i:x+1], logi[i+2:x-1]
    except:
        return logi,logi
        
def solve(logi):
    while ((logi != 'T') and (logi !='F')):
        logi1, logi2 = bracket_eval(logi,0)
        logi2 = logic_eval(logi2)
        logi = logi.replace(logi1,logi2)
    return logi


#Recursively replace each variable with a boolean (T,F) and keep testing for all possible combinations.
#If a contingency occurs. Return directly and set each boolean to True if possible
def find_truth(logi, Vars_array, count):
    global Contin, Tautol, Contra
    count += 1
    
    #Check if we are at the last point in our array eg P=[P1,P2], last point is P2
    if count == len(Vars_array):
        new_logi = logi.replace(Vars_array[count - 1], 'T')
       	#print ("IF1 STATEMENT: ", new_logi)
        solve_logi = solve(new_logi)

        if solve_logi == 'T':
            Tautol = True
        elif solve_logi == 'F':
            Contra = True

        if Tautol == True and Contra == True:
            Contin = True
            return

        new_logi = logi.replace(Vars_array[count - 1], 'F')
        #print ("IF2 STATEMENT: ", new_logi)
        solve_logi = solve(new_logi)
        #print ("Solution: ", solve_logi)

        if solve_logi == 'T':
            Tautol = True
        elif solve_logi == 'F':
            Contra = True

        if Tautol == True and Contra == True:
            Contin = True
            return

        return
    #Otherwise recursively call function until we reach end variable, finding the truth table for each variable
    else:
        new_logi = logi.replace(Vars_array[count - 1], 'T')
       	#print ("IF1 ELSE STATEMENT: ", new_logi)
        find_truth(new_logi, Vars_array, count)

        if Contin == True:
            return

        new_logi = logi.replace(Vars_array[count - 1], 'F')
       	#print ("IF2 ELSE STATEMENT: ", new_logi) 
        find_truth(new_logi, Vars_array, count)

        if Contin == True:
            return

        return
    

#Print our results    
def print_res(logi, Vars_array):
    global Tautol, Contin, Contra, count

    # Set Booleans back to False and initialize array to the beginning.
    Tautol = False
    Contin = False
    Contra = False
    count = 0
    
    #Call Our recursive Function
    find_truth(logi, Vars_array, count)
    
    if Contin:
        print("The compound proposition is a Contingency")
    elif Tautol:
        print("The compound proposition is a Tautology")
    elif Contra:
        print("The compound proposition is a Contradiction")
    else:
        print("Error")


#Print Table        
def table_generator(Vars_array, logi):
    print("Truth table:")
    print(" ")

    for x in range (0, len(Vars_array)):
        print (Vars_array[x], " ||  ", end="")
    print(logi)


    for x in range(0, 2 ** len(Vars_array)):
        line_array = (bin(x).replace("0b", "").zfill(len(Vars_array)))
        replaced_line = line_array.replace('1', 'T').replace('0', 'F')
        Vals_array = list(replaced_line)
        propositionOfLineReplaced = logic_val(Vars_array, Vals_array, logi)
        print(*replaced_line,"\t", solve(propositionOfLineReplaced), sep="\t")


        
print ("Enter propositional variables P = [P1,P2,...Pn] and a sentence in each of the inputs")
print (" Example: \nP1,P2\n( - P1 AND ( P1 OR P2 ) ) THEN P2")

Variables = input("Enter propositional variables: ")
logic =  input("Enter a logical sentence: ")
Variables,logic = fix_array(Variables,logic)
print_res(logic, Variables)
table_generator(Variables, logic)