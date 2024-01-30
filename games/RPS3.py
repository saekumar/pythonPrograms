import random
comList=["rock","paper","scissor"]
player=None
com=random.choice(comList)
s=True
while s:
    player=input("Rock Paper Scissor ? : ").lower()
    if player=='n':
        break
    elif player not in comList:
        print(" Just type Rock Paper Scissor ?")
        continue
    elif player in comList:
       if player==com:
        print("PLAYER :"+player)
        print("COMPUTER :"+com)
        print("ITS DRAWW...🤷‍♂️😁")
       elif player=="scissor":

        if com=="paper":
            print("PLAYER :"+player)
            print("COMPUTER :"+com)
            print("YOU WONN..✌😎❤")
        else:
            print("PLAYER :"+player)
            print("COMPUTER :"+com)
            print("YOU LOSE...😜😂")
       elif player=="paper":
        
        if com=="rock":
            print("PLAYER :"+player)
            print("COMPUTER :"+com)
            print("YOU WONN..✌😎❤")
        else:
            print("PLAYER :"+player)
            print("COMPUTER :"+com)
            print("YOU LOSE...😜😂")
       elif player=="rock":
        if com=="scissor":
            print("PLAYER :"+player)
            print("COMPUTER :"+com)
            print("YOU WONN..✌😎❤")
        else:
            print("PLAYER :"+player)
            print("COMPUTER :"+com)
            print("YOU LOSE...😜😂")     
            
            