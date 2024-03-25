#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	string str, b; cin >> str >> b;
	vector<char> v;
	bool check = false;
	int targetLen = b.length();
	for (int i = 0; i < str.length(); i++) {
		v.push_back(str[i]);
		if (v.size() >= targetLen) {
			for (int j = 0; j < targetLen; j++) {
				if (v[v.size() - targetLen + j] == b[j]) {
					check = true;
				}
				else {
					check = false;
					break;
				}
			}
			if (check) {
				v.erase(v.end()-targetLen,v.end());
			}
		}
	}
	if (!v.size()) cout << "FRULA";
	else {
		for (auto c : v) {
			cout << c;
		}
	}
}