#include <iostream>
using namespace std;

int main() {
	int n; cin >> n;
	int* arr = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	int t; cin >> t;
	int cnt = 0;

	for (int i = 0; i < n; i++) {
		if (arr[i] == t) {
			cnt++;
		}
	}
	cout << cnt;
}