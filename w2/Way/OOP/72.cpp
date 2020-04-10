#include <iostream>
#include <string>
using namespace std;

class Beket{
public:
	int x;
	int y;
	
	void print(){
		cout<<x<<" yes "<<y;
	}
private:
	int z;
	void printZ(){
		cout<<z<<"Hello mathfcka";
	}	
};

class Football{
public:
	string name;
	string a;
	string height;
	string team;
	string position;
	int age;
	int number;
};

int main()
{
	
	Beket Kane;
	Kane.x = 4;
	Kane.print();
	cout<<Kane.x<<endl;



	Football player;
	player.name = "Beket";
	player.height = "184cm";
	player.team = "FC Real Madrid";
	player.position = "ST,CF,LW,RW,CAM";
	player.age = 21;
	player.number = 7;

	cout<<player.name<<endl<<player.height<<endl<<player.team<<endl<<player.position<<endl<<player.age<<endl<<player.number<<endl;

	return 0;
}