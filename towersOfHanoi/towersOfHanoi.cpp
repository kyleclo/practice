#include <iostream>
#include <stack>

using namespace std;

class Tower{

	public:
		Tower(int, char);
		Tower();
		~Tower();
		void MoveTopTo(Tower&);
		void PrintCurrentState();

	private:
		stack <int> tower;
		char name;
};


Tower::Tower(int numberOfDisks, char letter){

	// initialize tower disks (from bottom to top) [numberOfDisks, ..., 2, 1]
	for(int i = numberOfDisks; i > 0; i--)
		tower.push(i);

	name = letter;
}


Tower::Tower(){
}


Tower::~Tower(){
}


void Tower::MoveTopTo(Tower& targetTower){

	if(!tower.empty()){
		int disk  = tower.top();
		tower.pop();
		targetTower.tower.push(disk);

		cout << "Moved top-most disk (" << disk << ") from Tower " << name << " to " << targetTower.name << "." << endl;
	}
}


void Tower::PrintCurrentState(){

	cout << "Tower " << name << " has " << tower.size() << " disks." << endl;

	stack <int> temp;

	cout << "The disks (from top to bottom) are:";
	while(!tower.empty()){
		cout << " " << tower.top();
		temp.push(tower.top());
		tower.pop();
	}
	cout << endl;

	while(!temp.empty()){
		tower.push(temp.top());
		temp.pop();
	}
}


void SolveTowersOfHanoi(int, Tower&, Tower&, Tower&);


int main(int argc, char** argv){

	int numberOfDisks = 5;
	Tower tower[3];
	tower[0] = Tower(numberOfDisks, 'a');
	tower[1] = Tower(0, 'b');
	tower[2] = Tower(0, 'c');

	cout << "Initial state of towers:" << endl;
	tower[0].PrintCurrentState();
	tower[1].PrintCurrentState();
	tower[2].PrintCurrentState();
	cout << endl;

	SolveTowersOfHanoi(numberOfDisks, tower[0], tower[1], tower[2]);
	cout << endl;

	cout << "End state of towers:" << endl;
	tower[0].PrintCurrentState();
	tower[1].PrintCurrentState();
	tower[2].PrintCurrentState();
	cout << endl;

	return 0;
}


void SolveTowersOfHanoi(int numberOfDisks, Tower& start, Tower& middle, Tower& end){

	if(numberOfDisks > 0){
		SolveTowersOfHanoi(numberOfDisks - 1, start, end, middle);
		start.MoveTopTo(end);
		SolveTowersOfHanoi(numberOfDisks - 1, middle, start, end);
	}
}

