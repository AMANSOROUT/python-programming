#guess the number

Score=10
import random
computer_number= random.randrange(1,101)

while True:
    user_no=int(input('Guess the number 1 to 100'))
    if user_no==computer_number:
        print('you Win and your score is',Score)
        break
    elif user_no> computer_number:
        print('you Lose and your No. is larger than the actual value')
    elif Score<1:
        print('you loose and your score is',Score)
        break
    else:
        print('you Lose and your No. is smaller than the actual value')
    Score-=1
        
    

    
