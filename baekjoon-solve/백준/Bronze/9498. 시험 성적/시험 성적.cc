#include <iostream>
using namespace std;

int main() {
	int s;
	cin >> s;
	int c = s / 10;
	if (c > 8) {
		cout << 'A';
	}
	else if (c == 8) {
		cout << 'B';
	}
	else if (c == 7) {
		cout << 'C';
	}
	else if (c == 6) {
		cout << 'D';
	}
	else { cout << 'F'; }
}