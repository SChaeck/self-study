#include <iostream>
#include <stack>
#include <queue>
using namespace std;

int main() {
	int n; cin >> n; // n 입력 받기
	int* targetArr = new int[n]; 
	for (int i = 0; i < n; i++) { // 수열 입력 받음
		cin >> targetArr[i];
	} 
	stack<int> stk; // 문제해결에 사용할 스택 생성
	queue<char> que; // 출력 값을 저장할 큐 생성 
	int check = 1;

	for (int i = 0; i < n; i++) { // 목표 수열을 돌면서 push, pop 확인
		while (check <= targetArr[i]) {
			que.push('+');
			stk.push(check);
			check++;
		}
		if (stk.top() == targetArr[i]) {
			que.push('-');
			stk.pop();
		}
		else {
			cout << "NO";
			return 0;
		}
	}
	while (!que.empty()) {
		cout << que.front() << '\n';
		que.pop();
	}

	delete[] targetArr;
}