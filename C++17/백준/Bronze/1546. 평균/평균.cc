#include <iostream>
using namespace std;

int main() {
	int n; cin >> n;
	float sum = 0;
	float num;
	float max = 0;
	for (int i = 0; i < n; i++) {
		cin >> num;
		if (num > max) max = num;
		sum += num;
	}
	cout << sum * 100 / max / n;
}