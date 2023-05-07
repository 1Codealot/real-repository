#include<iostream>
#include<cstdlib>
using namespace std;

int getRandomNum(){
	srand((unsigned) time(NULL));

	int random = rand()%10;

	return random;

}

void gameplay()
{
	//Set up
	int numToGuess = getRandomNum();
	int guesses = 5;
	int pGuess;

	while (guesses > 0)
	{
		cout<<"Guess a number between 0 and 10. You have "<<guesses<<" guesses remaining."<<endl;
		cin>>pGuess;

		if (pGuess > numToGuess)//too big
		{
			cout<<"Too high!"<<endl;
		}
		else if (pGuess < numToGuess)
		{
			cout<<"Too low!"<<endl;
		}
		else //Must be equal then.
		{
			cout<<"You win!!"<<endl;
			break;
		}
	guesses -= 1;
	}

	if (guesses==0)
	{
		cout<<"You lose! The number was "<<numToGuess<<"."<<endl;
	}
}

int main()
{
	string gaming = "Y";

	while(gaming == "Y" || gaming == "y")
	{
		gameplay();
		cout<<"Play again? (Yes or No)"<<endl;
		cin>>gaming;
		gaming = gaming[0];

	}
	cout<<"Thanks for playing!!";

	return 0;
}