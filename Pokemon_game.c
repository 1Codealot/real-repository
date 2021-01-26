#include <stdio.h>
#include <stdlib.h> //For the RNG
#include <conio.h> //Console I/O

int main()

//NOTE TO SELF PRESS BUILD AND RUN
//DON'T FORGET SEMI COLONS

{
    //Start off by making the vars for health
    int p1_health = 100;
    int ai_health = 100;
    char move;
    //Now for damage
    int ember = 5;
    int inferno = 15;
    int counter = 0;
    //RNG stuff
    int i, n;
    time_t t;

    //Now to make a "UI"
    printf("Hi are you ready to play? If this is your first time playing, type 'h' (press 'h' and then enter) if you are ready to play, press any other button ");
    char start_up;

    start_up=getche();

    if (start_up=='h'){

        printf("Hi! Than you for playing! I hope you enjoy this game! \nInstructions: \nThere are 2 moves, 'Ember' and 'Inferno' \nIf you want to use 'Ember' type 'e' or if you want to use 'Inferno' type'i'  \nNote: This is not at all perfect you may have to type the letter for the move twice. \n Thanks for playing!\n\n");
    }

//Game start
    while(p1_health > 0 && ai_health > 0){
//Player one's go

        printf("You have %d HP" ,p1_health);
        printf(" and the computer has %d HP\n" ,ai_health);

        printf("Choose your move: type 'e' for ember or 'i' for inferno\n");
        move=getche();
        //printf("\ninput: >%c<\n", move);
        printf("\n%c is your move\n", move);
        if(move=='e'){
            ai_health = ai_health-5;

            }
        else if(move=='i'){
            ai_health=ai_health-15;

        }
//AI's move
        n = 1;

        srand((unsigned) time(&t));

        for(i=0 ; i < 1 ; i++)
        {
            int rand_test = rand() % 2;
            //printf("%d\n", rand_test);
            if(rand_test==0){
                printf("AI's chosen move is Ember\n");
                p1_health = p1_health-5;
            }
            else if(rand_test==1){
                printf("AI's chosen move is Inferno\n");
                p1_health = p1_health-15;
            }


        }


    }

    if (ai_health <= 0){
        printf("You Win!!");

    }

    else if (p1_health <= 0){

        printf("AI wins");
    }


    return 0;
}
