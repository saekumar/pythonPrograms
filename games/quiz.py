def new_game():
    guesses=[]
    crct_guesses=0
    qsnnmbr=1


    for key in qsns:
        print("___________________")
        print(key)  
        for i in options[qsnnmbr-1]:
            
            print(i)
        gues=input(("Enter A B C D: ")).upper()
        guesses.append(gues)

        
        crct_guesses+=check_ans(qsns.get(key),gues)
        qsnnmbr+=1
    display_score(crct_guesses,guesses)

#_________________________________________________

def check_ans(ans,gues):
    if ans==gues:
        print("CORRECT!!!!")
        return 1
    else:
        print("WRONG!!!")
        return 0
#_________________________________________________
def display_score(crct_guesses,guesses):
    print("___________")
    print("RESULTS")
    print("___________")
    print("CORREECT ANSWERS :")
    for key in qsns:
        print(qsns.get(key)+" ",end="")
    print()
    print("YOUR GUESSES : ")
    for i in guesses:
        
        print(i+" ",end="")
    print()
    score=int((crct_guesses/len(qsns))*100)
    print("YOUR SCORE: "+str(score)+"%")


    
#_________________________________________________
def play_again():
    res=input("U WANNA PLAY AGAIN? (Y/N) : ")
    res=res.upper()
    if res=="Y":
        return True

    else:
        return False





#_________________________________________________
qsns={
    "WHAT IS UR NAME?: ":"A","WHICH YEAR U BORN ? :":"B","UR GENDER ? ": "C","EARTH ROUND ? :": "A"
}
options=[["A.Telidhu","B.Cheppanu","C.Cheppalenu","D.Cheppakudadhu"],

         ["A.Gandhi thatha na thamudu","B.Sachii padhi rojulu ayyindhi","C.Nen inka puttaledhu","D. MA Amma ni adigi chepthaa.."],
         ["A.Telidhu","B.Marchipoyaa","C.Cheppalenu","D.Cheppakudadhu"],
         ["A.Avnu","B.Kadhu","C.Evadki thelsehee","D.Nelaa Baaru"]]

new_game()
while play_again():
    new_game()

