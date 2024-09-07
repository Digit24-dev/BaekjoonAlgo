#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <memory.h>

using namespace std;

#define cord pair<int, int>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);

#define MAX 1000 + 1

int N;
vector<string> words;

int main()
{
    FASTIO

    cin >> N;
    words.resize(N);
    for (size_t i = 0; i < N; i++)
        cin >> words[i];
    
    sort(words.begin(), words.end(), [](string a, string b) {
        if (a.size() == b.size()) {
            int _a = 0, _b = 0;
            for (size_t i = 0; i < a.size(); i++)
            {
                char __a = a[i], __b = b[i];
                _a += isdigit(__a) ? (__a - '0') : 0;
                _b += isdigit(__b) ? (__b - '0') : 0;
            }
            
            if (_a == _b) {
                return a < b;
            }else
                return _a < _b;
            
        } else {
            return a.size() < b.size();
        }
    });

    for (auto elem : words)
    {
        cout << elem << endl;
    }

    return 0;
}