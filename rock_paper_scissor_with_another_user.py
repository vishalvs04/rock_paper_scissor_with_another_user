import random
def play_rock_paper_scissor():
    runner_code=True
    user1_score=0
    user2_score=0
    while runner_code:
        choices=['rock','paper','scissor']
        user1_choice=input("USER 1 Choose Rock, Paper or Scissor, OR q for quitting: ")
        user2_choice=input('USER 2 Choose Rock, Paper or Scissor, OR q for quitting: ')

        if user1_choice==user2_choice and (user1_choice!='q' and user2_choice!='q'):
            print('Its A TIE!!!!')
        elif user1_choice=='rock' and user2_choice=='paper':
            print('Paper covers Rock, User2 Wins')
            user2_score+=1
            print('User 1 Score=',user1_score)
            print("User 2 Score=",user2_score)
        elif user1_choice=='scissor' and user2_choice=='rock':
            print('Rock Breaks Scissor, User2 Wins')
            user2_score+=1
            print('User 1 Score=',user1_score)
            print("User 2 Score=",user2_score)
        elif user1_choice=='paper' and user2_choice=='scissor':
            print('Scissor Cuts Paper, User2 Wins')
            user2_score+=1
            print('User 1 Score=',user1_score)
            print("User 2 Score=",user2_score)
        elif user1_choice=='paper' and user2_choice=='rock':
            print("Paper Covers Rock, User1 Wins")
            user1_score+=1
            print('User 1 Score=',user1_score)
            print("User 2 Score=",user2_score)
        elif user1_choice=='rock' and user2_choice=='scissor':
            print('Rock breaks Scissor, User1 Wins')
            user1_score+=1
            print('User 1 Score=',user1_score)
            print("User 2 Score=",user2_score)
        elif user1_choice=='scissor' and user2_choice=='paper':
            print('Scissor cuts paper, User1 Wins')
            user1_score+=1
            print("User 1 Score=",user1_score)
            print("User 2 Score=",user2_score)
        elif user1_choice=='q' or user2_choice=='q':
            if user1_score>0 or user2_score>0:
                print("User 1 Score=",user1_score)
                print("User 2 Score=",user2_score)
            print('Quit')
            runner_code=False