#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <memory.h>

using namespace std;

#define cord pair<int, int>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);

#define MAX 15 + 1

vector<pair<int, int>> table;
int dp[MAX];
int N;

// solution
// 2. DP

void input()
{
    cin >> N;
    for (size_t i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;
        table.push_back(make_pair(a, b));
    }
}

void solution()
{
    // 뒤에서 부터 탐색
    for (int i = N-1; i >= 0; i--)  // size_t로 선언하여 사용하게 되면, i는 항상 0보다 크게된다... 생각해서 사용하자.
    {
        int deadline = i + table[i].first;
        // 1. 현재 first가 남은 일 수 보다 큰지 확인할 것
        if (deadline > N)
            dp[i] = dp[i+1];
        else 
            dp[i] = max(dp[i+1], table[i].second + dp[deadline]);
    }
}

int main()
{
    FASTIO

    input();

    solution();
    
    cout << dp[0] << endl;

    return 0;
}
