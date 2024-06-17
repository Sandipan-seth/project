# 1 for stone
# 2 for paper 
# 3 for scissor
import random
meaning={
    1:"Stone",
    2:"paper",
    3:"scissor"
}
print("\n\t THIS STONE PAPER SCISSOR GAME IS BEST OF 3 \n\t 1 for stone \n\t 2 for paper \n\t 3 for scissor:")
i=0
yScore=0
compScore=0
while (i<3):
    computer=random.choice([1,2,3])
    you=int(input("Enter your choice:"))
    if(you<1 or you>3):
        raise ValueError("value should be in between 1 to 3")
    print(f"You choose {meaning[you]} and computer choose {meaning[computer]}")
    if(computer==you):
        print("\t Its a draw")
    else:
        if((computer==3 and you ==1)or(computer==1 and you==2)or(computer==2 and you==3)):
            print("\tYou Won")
            yScore+=1
        elif((computer==1 and you ==3)or(computer==2 and you==1)or(computer==3 and you==2)):
            print("\tComputer won")
            compScore+=1

    i=i+1
if(yScore>compScore):
    print(f"\n\n\t You win!! and your score is {yScore} and computer score is {compScore}")
elif(compScore>yScore):
    print(f"\n\n\t Computer win!! and your score is {yScore} and computer score is {compScore}")
else:
    print(f"\n\n\t Its a draw and your score is {yScore} and computer score is {compScore}")
    
