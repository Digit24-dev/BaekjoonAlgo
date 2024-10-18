#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <limits.h>

#define endl    '\n'
// #define INT_MAX 2,147,483,648

using namespace std;

int N;

int main()
{
    cin >> N;
    long ans = 0;
    stack<pair<int, int>> s;
    s.push({INT_MAX, 0});

    for (int i = 0; i < N; i++)
    {
        int heigth;
        cin >> heigth;
        int inner_cnt = 0;

        while (s.top().first < heigth)
        {
            ans += s.top().second;
            s.pop();
        }
        
        if (s.top().first == heigth)
        {
            inner_cnt = s.top().second;
            ans += inner_cnt;
            s.pop();
            if (s.top().second != 0)
                ans++;
            s.push({heigth, inner_cnt + 1});
        }
        else if (s.top().first > heigth)
        {
            if (s.top().second != 0)
                ans++;
            s.push({heigth, 1});
        }

    }
    
    cout << ans << endl;

    return 0;
}