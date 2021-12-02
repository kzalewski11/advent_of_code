#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int expenses[1000];
	int cur = 0;
	int expense;
	ifstream in ("./input.txt");

	while (in >> expense) {	expenses[cur++] = expense; }
	in.close();

	int solution;
	for (int i=0; i<cur-2; i++) {
		for (int j=i+1; j<cur-1; j++) {
			for (int k=j+1; k<cur; k++) {
				if (expenses[i] + expenses[j] + expenses[k] == 2020) {
					solution = expenses[i] * expenses[j] * expenses[k];
					break;		
				}
			}
		}
	}
	cout << solution << endl;
			
	return 0;
}
