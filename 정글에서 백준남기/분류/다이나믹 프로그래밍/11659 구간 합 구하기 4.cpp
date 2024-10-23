#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>

#define FASTIO  cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
#define endl '\n'

using namespace std;

int N, M;
int dp[100001];

int main()
{
    FASTIO
    
    cin >> N >> M;
    for (int i = 0; i < N; i++)
        cin >> dp[i];
    
    for (int i = 1; i < N; i++)
        dp[i] += dp[i-1];

    for (int k = 0; k < M; k++)
    {
        int i, j;
        cin >> i >> j;
        cout << dp[j-1] - dp[i-2] << endl;
    }
    
    return 0;
}