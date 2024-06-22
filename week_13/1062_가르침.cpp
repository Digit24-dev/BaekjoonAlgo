#include <iostream>
#include <string>
#include <memory.h>
#include <vector>
#include <algorithm>

using namespace std;

bool ch[26];
int N, K, maxReadable;
vector<string> words;

void input() {
    for (size_t i = 0; i < N; i++)
    {
        cin >> words[i];
        words[i] = words[i].substr(4, words[i].size() - 8);
    }
}

void dfs(int index, int count)
{
    if (K == count) {
        // 배운 글자들로 읽을 수 있는 단어 개수 count
        int readable = 0;
        for (const string& word: words) {
            bool canRead = true;
            for (auto c : word)
            {
                if (!ch[c - 'a']) {
                    canRead = false;
                    break;
                }
            }
            if (canRead) readable++;
        }
        maxReadable = max(maxReadable, readable);
        return;
    }

    for (int i = index; i < 26; i++)
    {
        if (!ch[i]) {
            ch[i] = true;
            dfs(i + 1, count + 1);
            ch[i] = false;
        }
    }
}

int main() {

    cin >> N >> K;

    if (K < 5) {
        cout << 0 << endl;
        return 0;
    }

    words.resize(N);
    input();

    ch['a' - 'a'] = true;
    ch['c' - 'a'] = true;
    ch['i' - 'a'] = true;
    ch['n' - 'a'] = true;
    ch['t' - 'a'] = true;
    
    dfs(0, 5);

    cout << maxReadable << endl;

    return 0;
}