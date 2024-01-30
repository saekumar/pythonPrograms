import random
choices=["rock","paper","scissor"]
com=random.choice(choices)
player=None
while player not in choices:
    player=input("ROCK,PAPER,SCISSOR ?: ").lower()
if player==com:
    print("PLAYER : "+player)
    print("COMPUTER : "+com)
    print("ITS DRAW...🤷‍♂️")
elif player=="scissor":
    if com=="rock":
        print("PLAYER : "+player)
        print("COMPUTER : "+com)
        
        print("YOU LOSE...😂😜")
    else:
        print("PLAYER : "+player)
        print("COMPUTER : "+com)
        print("YOU WIN...✌😎")
elif player=="rock":
    if com=="paper":
        print("PLAYER : "+player)
        print("COMPUTER : "+com)
        print("YOU LOSE...🤣🤣")
    else:
        print("PLAYER : "+player)
        print("COMPUTER : "+com)
        print("YOU WIN...✌😎")
elif player=="paper":
    if com=="scissor":
        print("PLAYER : "+player)
        print("COMPUTER : "+com)
        print("YOU LOSE...🤣🤣")
    else:
        print("PLAYER : "+player)
        print("COMPUTER : "+com)
        print("YOU WIN...✌😎")