def split_array(Vars,Vals):
    variable_array = Vars.split(',')
    values_array = Vals.split(',')
    return variable_array, values_array

def logic_val(Vars_array,Vals_array,logi):
    varval = dict(zip(Vars_array,Vals_array))
    for P,V in varval.items():
        logi = logi.replace(P,V)
    
    logi = logi.replace('TRUE', 'T')
    logi = logi.replace('FALSE', 'F')
    return logi



def logic_eval(logi):
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
       
        
    #Evalute compliment
    #while '-' in logi:
    logi = logi.replace('- F', 'T')
    logi = logi.replace('- T', 'F')

    #Evaluate 'THEN'
    #while 'THEN' in logi:
    logi = logi.replace('T THEN F', 'F')
    logi = logi.replace('T THEN T', 'T')
    logi = logi.replace('F THEN F', 'T')
    logi = logi.replace('F THEN T', 'T')
        
    #Evaluate '='
    #while 'EQUALS' in proposition:
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
#         print(logi)
#         print(len(logi))
    return logi
	
print ("Enter propositional variables P = [P1,P2,...Pn] with their truth values and a sentence in each of the inputs")
print ("Example: \nP1,P2,P3\nT,T,T\n( ( P1 AND P2 ) OR ( P3 AND TRUE ) ) OR ( ( - P1 AND - P3 ) AND P2 )")
a =[]
b =[]
while ( (not a) or (len(a) != len(b)) ):
    Variables = input("Enter propositional variables: ")
    Values = input("Enter truth values: ")
    a, b = split_array(Variables, Values)
    if len(a) != len(b):
        print("Please enter valid inputs")
logic =  input("Enter a logical sentence: ")

logic2 = logic_val(a,b, logic)
print(logic2)
logic2 = solve(logic2)
if logic2 == 'T':
    print(True)
elif logic2 == 'F':
    print(False)