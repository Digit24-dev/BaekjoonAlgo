#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <memory.h>

using namespace std;

#define cord pair<int, int>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);

#define MAX 1000 + 1

vector<pair<int, int>> table;
int N;
int ans;

// solution
// 1. 완전 탐색

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

void dfs(int cur, int cost) 
{
    // 종료 조건
    if (cur >= N)
    {
        ans = max(ans, cost);
        return;
    }
    
    // 오늘은 상담을 한 날.
    if (cur + table[cur].first <= N)
        dfs(cur + table[cur].first, cost + table[cur].second);

    // 상담을 하지 않은 날은 + 1.
    if (cur + 1 <= N)
        dfs(cur + 1, cost);
}

int main()
{
    FASTIO

    input();

    dfs(0, 0);
    
    cout << ans << endl;

    return 0;
}
