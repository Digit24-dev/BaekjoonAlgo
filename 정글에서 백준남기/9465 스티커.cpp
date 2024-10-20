#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <limits.h>

#define endl    '\n'

using namespace std;

int desk[2][100001];
int dp[2][100001];
int T, N;

void debug()
{
    // debug
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    cin.tie(0); ios::sync_with_stdio(0);

    cin >> T;
    while (T--)
    {
        // cout << "#" << T << endl;
        // input
        cin >> N;
        for (int i = 0; i < 2 * N; i++)
        {
            cin >> desk[i / N][i % N];
        }

        // solution
        // dp[0][0] 부터 시작
        dp[0][0] = desk[0][0];
        dp[1][0] = desk[1][0];
        int prev = 0;
        int iprev = 1;
        for (int i = 1; i < N; i++)
        {
            dp[prev][i] = dp[iprev][i - 1] + desk[prev][i];
            dp[iprev][i] = dp[prev][i - 1] + desk[iprev][i];

            if (i > 1) {
                int m_prev = max(dp[prev][i - 2], dp[iprev][i - 2]);
            
                if (m_prev + desk[prev][i] > dp[iprev][i - 1] + desk[prev][i])
                    dp[prev][i] = m_prev + desk[prev][i];

                if (m_prev + desk[iprev][i] > dp[prev][i - 1] + desk[iprev][i])
                    dp[iprev][i] = m_prev + desk[iprev][i];
            }
        }

        cout << max(dp[0][N - 1], dp[1][N - 1]) << endl;
    }


    return 0;
}