#include <iostream>
#include <queue>
using namespace std;

int main() {
	int n, k; cin >> n >> k;
	queue<int> que;
	int* arr = new int[n+1];
	int check = 0;
	for (int i = 1; i <= n; i++) {
		que.push(i);
	}
	for (int i = 1; que.size() > 0; i++) {
		if (i % k == 0) {
			arr[check++] = que.front();
			que.pop();
		}
		else {
			que.push(que.front());
			que.pop();
		}
	}
	cout << '<';
	for (int i = 0; i < n; i++) {
		if (i == n - 1) {
			cout << arr[i] << '>';
		}
		else cout << arr[i] << ", ";
	}

	delete[] arr;
}