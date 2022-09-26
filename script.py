import pandas as pd



def addApplicant():
    
    name = input("Applicant's Full Name: ")
    tab["Full Name"].append(name)
    print("Rate the following aspects with a score from 1 to 5:")
    res = int(input("Personality: "))
    tab["Personality"].append(res)
    res = int(input("Reasoning: "))
    tab["Reasoning"].append(res)
    res = int(input("Confidence: "))
    tab["Confidence"].append(res)
    res = int(input("Social Skills: "))
    tab["Social Skills"].append(res)
    res = int(input("Honesty: "))
    tab["Honesty"].append(res)
    cmnt = input("""If you have any additional comments or remarks leave them down here:
    |>> """)
    if(cmnt == ""):
        cmnt = "None"
    tab["Additional Comments"].append(cmnt)

def addApplicants():
    global tab
    tab = {"Full Name":[], "Personality":[], "Reasoning":[], "Confidence":[], "Social Skills":[], "Honesty":[], "Additional Comments":[]}
    df1=pd.read_csv("applicants.csv")
    dic = df1.to_dict()
    for i in range(0, len(dic['Full Name'])):
        tab["Full Name"].append(dic["Full Name"][i])
        tab["Personality"].append(dic["Personality"][i])
        tab["Reasoning"].append(dic["Reasoning"][i])
        tab["Confidence"].append(dic["Confidence"][i])
        tab["Social Skills"].append(dic["Social Skills"][i])
        tab["Honesty"].append(dic["Honesty"][i])
        tab["Additional Comments"].append(dic["Additional Comments"][i])

    done = False
    while not done:
        addApplicant()
        resp = input("Do you still want to add more applicants? (Y/N)")
        if(resp == 'N'):
            done = True
        elif(resp == 'Y'):
            pass
        else:
            print("Invalid Choice."); break;
    
    f = open("applicants.csv", "w")
    df = pd.DataFrame(tab)
    f.write(pd.DataFrame.to_csv(df, index=False))
    print("Applicant's info has been added successfully !")
    f.close()
def listApplicant():
    df=pd.read_csv("applicants.csv")
    dic = df.to_dict()
    name = input("What is the name of the applicant you want to list?\n|>> ")
    for i in range(0, len(dic['Full Name'])):
        if(name.upper() == str(dic["Full Name"][i]).upper()):
            print(f"Full Name: {name}")
            pers = dic["Personality"][i]
            print(f"Personality: {pers}")
            pers = dic["Reasoning"][i]
            print(f"Reasoning: {pers}")
            pers = dic["Confidence"][i]
            print(f"Confidence: {pers}")
            pers = dic["Social Skills"][i]
            print(f"Social Skills: {pers}")
            pers = dic["Honesty"][i]
            print(f"Honesty: {pers}")
            pers = dic["Additional Comments"][i]
            print(f"Additional Comments: {pers}")
            break
    print(i)
    if( i >= len(dic["Full Name"]) - 1):
        print("No applicant found. :(")

def listAll():
    df=pd.read_csv("applicants.csv")
    print(df.to_string(index=False))


def menu():
    done = False
    while not done:
        
            inp = int(input(""" Menu:
            [1] Add Applicant Info
            [2] Consult Applicant Info
            [3] List all applicants and their info
            [4] Quit
            |>> """))
            if(inp == 1):
                addApplicants()
            elif(inp == 2):
                listApplicant()
            elif(inp == 3):
                listAll()
            elif(inp == 4):
                done = True
            else:
                print("Invalid choice.")
        
menu()