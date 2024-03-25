#include <iostream>
using namespace std;

int main() {
	int h, m, t;
	cin >> h >> m >> t;
	int th = t / 60;
	int tm = t % 60;
	m = m + tm;
	if (m >= 60) {
		m = m - 60;
		h += 1;
	}
	h = h + th;
	if (h >= 24) {
		h = h - 24;
	}
	cout << h << " " << m;
}