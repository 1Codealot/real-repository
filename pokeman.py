# POKEMON STYLE GAME!
import random
import time

''' How it works:

The program will ask user for 1p or 2p
if it is 1p:
    user will be asked for a move (Ember or Inferno)
    chooses a random number to determine if it is critical
    wait 0.25 secs
    "ai" chooses a random move
    chooses a random number to determine if it is critical
    wait 0.25 secs
    repeats until someones health is 0 or less
or if it is 2p:
    p1 will be asked for a move
    chooses a random number to determine if it is critical
    wait 0.25 secs
    p2 will be asked for a move 
    chooses a random number to determine if it is critical
    wait 0.25 secs
'''

def one_player():
    p1_health=100
    ai_health=100
    while p1_health>0 and ai_health>0:
        while True:
            move= input('P1, choose yoour move (Ember or Inferno MUST have a capital letter at the start)\n>>>')
            if move=='Ember'or move=='ember':
                critical=random.randint(0,15)
                if critical==11:
                    ai_health=ai_health-15
                    print('You used Ember! \nCritical Hit! \nOpponent\'s health is',ai_health)
                    break
                else:
                    ai_health=ai_health-5
                    print('You used Ember!\nopponent\'s health is',ai_health)
                    break
            elif move == 'Inferno' or move == 'inferno':
                critical=random.randint(0,15)
                if critical==11:
                    ai_health=ai_health-25
                    print('You used Inferno!\nCritical Hit!\nopponent\'s health is',ai_health)
                    break
                else:
                    ai_health=ai_health-15
                    print('You used Inferno!\nopponent\'s health is',ai_health)
                    break
        time.sleep(0.25)
        if p1_health <=0: #p1 lost
            print('Game Over! AI Wins!')
            break
        elif ai_health <=0: #AI lost
            print('Game Over! P1 Wins!')
            break

       
        # AI'S GO

        move=random.randint(1,2)
        if move == 1:
            critical=random.randint(0,15)
            if critical==11:
                p1_health=p1_health-15
                print('Ai used Ember! \nCritical Hit! \np1\'s health is',p1_health)
            else:
                p1_health=p1_health-5
                print('Ai used Ember!\np1\'s health is',p1_health)
        else:
            critical=random.randint(0,15)
            if critical==11:
                p1_health=p1_health-25
                print('Ai used Inferno!\nCritical Hit!\nP1\'s health is',p1_health)
            else:
                p1_health=p1_health-15
                print('Ai used Inferno!\nP1\'s health is',p1_health)
        time.sleep(0.25)
        if p1_health <=0: #p1 lost
            print('Game Over! AI Wins!')
            break
        elif ai_health <=0: #AI lost
            print('Game Over! P1 Wins!')
            break

def two_player():
    p1_health=100
    p2_health=100
    while p1_health>0 and p2_health>0:
        while True:
            move= input('P1, choose yoour move (Ember or Inferno MUST have a capital letter at the start)\n>>>')
            if move=='Ember'or move=='ember':
                critical=random.randint(0,15)
                if critical==11:
                    p2_health=p2_health-15
                    print('You used Ember! \nCritical Hit! \nOpponent\'s health is',p2_health)
                    break
                else:
                    p2_health=p2_health-5
                    print('You used Ember!\nopponent\'s health is',p2_health)
                    break
            elif move == 'Inferno' or move == 'inferno':
                critical=random.randint(0,15)
                if critical==11:
                    p2_health=p2_health-25
                    print('You used Inferno!\nCritical Hit!\nopponent\'s health is',p2_health)
                    break
                else:
                    p2_health=p2_health-15
                    print('You used Inferno!\nopponent\'s health is',p2_health)
                    break
        time.sleep(0.25)
        if p1_health <=0: #p1 lost
            print('Game Over! P2 Wins!')
            break
        elif p2_health <=0: #p2 lost
            print('Game Over! P1 Wins!')
            break

        #P2'S GO

    
        while True:
            move= input('P2, choose yoour move (Ember or Inferno MUST have a capital letter at the start)\n>>>')
            if move=='Ember'or move=='ember':
                critical=random.randint(0,15)
                if critical==11:
                    p1_health=p1_health-15
                    print('You used Ember! \nCritical Hit! \nOpponent\'s health is',p1_health)
                    break
                else:
                    p1_health=p1_health-5
                    print('You used Ember!\nopponent\'s health is',p1_health)
                    break
            elif move == 'Inferno' or move == 'inferno':
                critical=random.randint(0,15)
                if critical==11:
                    p1_health=p1_health-25
                    print('You used Inferno!\nCritical Hit!\nopponent\'s health is',p1_health)
                    break
                else:
                    p1_health=p1_health-15
                    print('You used Inferno!\nopponent\'s health is',p1_health)
                    break
        time.sleep(0.25)
        if p1_health <=0: #p1 lost
            print('Game Over! P2 Wins!')
            break
        elif p2_health <=0: #p2 lost
            print('Game Over! P1 Wins!')
            break

players=input('How many people are playing? (1 or 2)\n')
if players=='1':
    one_player()
elif players=='2':
    two_player()
