#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

#define MAX 1000001

int ans = 0;
int dp[MAX];
int dp_list[MAX];

int main()
{
    int X;

    cin >> X;
    dp[1] = 0;

    for (int i = 2; i <= X; i++)
    {
        dp[i] = dp[i-1] + 1;
        dp_list[i] = i - 1;

        if (i % 3 == 0 && dp[i] > dp[i/3] + 1)
        {
            dp[i] = dp[i/3] + 1;
            dp_list[i] = i/3;
        }
        if (i % 2 == 0 && dp[i] > dp[i/2] + 1)
        {
            dp[i] = dp[i/2] + 1;
            dp_list[i] = i/2;
        }
    }
    
    cout << dp[X] << endl;
    while (X != 0)
    {
        cout << X << " ";
        X = dp_list[X];
    }

    return 0;
}