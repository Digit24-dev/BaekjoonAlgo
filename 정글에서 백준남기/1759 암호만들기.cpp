#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>

#define endl    '\n'

using namespace std;

/*
최소 두 개의 자음, 한 개의 모음
*/

int L, C;
string line;
set<char> s;

// acistw
void dfs(int a, int b, string &bucket, int depth, int idx)
{
    bucket.push_back(line[idx]);
    if (s.find(line[idx]) != s.end())
        a++;
    else b++;

    if (depth >= L) {
        // cout << bucket << " || a:" << a << ",b:" << b << ", bucekt size:" << bucket.size() << endl;
        if (a >= 1 && b >= 2 && bucket.size() == L) {
            cout << bucket << endl;
        }
        return;
    }

    for (int i = idx + 1; i < C; i++)
    {
        dfs(a, b, bucket, depth + 1, i);
        bucket.pop_back();
    }
}

int main()
{
    s.insert('a');
    s.insert('e');
    s.insert('i');
    s.insert('o');
    s.insert('u');

    cin >> L >> C;
    line.resize(C);

    for (int i = 0; i < C; i++)
        cin >> line[i];

    sort(line.begin(), line.end());
    // cout << line << endl;

    string bucket = "";
    for (int i=0; i<=C - L; i++) {
        dfs(0, 0, bucket, 1, i);
        bucket = "";
    }

    return 0;
}