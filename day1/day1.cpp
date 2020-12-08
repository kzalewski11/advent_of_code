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
	for (int j=0; j<cur-2; j++) {
		for (int k=j+1; k<cur-1; k++) {
			for (int l=k+1; l<cur; l++) {
				if (expenses[j] + expenses[k] + expenses[l] == 2020) {
					solution = expenses[j] * expenses[k] * expenses[l];
					break;		
				}
			}
		}
	}
	cout << solution << endl;
			
	return 0;
}
