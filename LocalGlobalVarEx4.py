#LocalGlobalVarEx4.py

def learnML():
    crs1="ML" # Here crs1 is called Local Variable
    print("'{}' Applications Developed by Using '{}' Lang".format(crs1,lang))
    #print(crs2,crs3) cant access bcozx they are local to other Functions
    print("-"*50)
def learnDL():
    crs2="DL" # Here crs2 is called Local Variable
    print("'{}' Applications Developed by Using '{}' Lang".format(crs2,lang))
    # print(crs1,crs3) cant access bcozx they are local to other Functions
    print("-" * 50)
def learnAI():
    crs3="AI" # Here crs3 is called Local Variable
    print("'{}' Applications Developed by Using '{}' Lang".format(crs3,lang))
    # print(crs1,crs2) cant access bcozx they are local to other Functions
    print("-" * 50)
#main program
#learnML()--cant access lang variable Value
lang = "PYTHON" # here lang is called Global Variable
learnDL()
learnAI()