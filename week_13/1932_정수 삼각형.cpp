#include <iostream>
#include <algorithm>

using namespace std;

// #define BOTTOM_UP
#define MAX_N 500

int dp[MAX_N + 1][MAX_N + 1];
int N;

void debug()
{
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < i + 1; j++)
        {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
}

#ifdef BOTTOM_UP
int main()
{
    int temp, ans = 0;
    cin >> N;
    cin >> temp;
    dp[0][0] = temp;
    dp[1][0] = temp;
    dp[1][1] = temp;
    ans = temp;

    for (int i = 1; i < N; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            cin >> temp;
            
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + temp);
            ans = max(ans, dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + temp));
        }
    }
    
    // debug();

    cout << ans;

    return 0;
}

#else   // TOP_DOWN
int main()
{
    int temp, ans = 0;
    cin >> N;
    
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < i + 1; j++)
        {
            cin >> dp[i][j];
        }
    }
    
    for (int i = N - 1; i >= 0; i--)
    {
        for (size_t j = 0; j < i; j++)
        {
            
        }
        
    }
    
}

#endif

