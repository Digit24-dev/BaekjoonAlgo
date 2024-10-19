#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <limits.h>

#define endl    '\n'
// #define INT_MAX 2,147,483,648
#define MODE
using namespace std;


#ifdef MODE
int main()
{
    int N; int dp[31];

    cin >> N;
    
    if (N & 0x01)
        cout << 0 << endl;
    else
    {
        // dp[6] = dp[4] * dp[2] + dp[2] * 2 + 2 = dp[4] * 3 + do[2] * 2 + 2
        // dp[N] = 3*dp[N-2] + 2*dp[N-4] + ... 2*dp[0] (dp[0] = 1)

        dp[0] = 1;
        dp[1] = 0;
        dp[2] = 3;
        for (int i = 4; i <= N; i += 2)
        {
            dp[i] = dp[i - 2] * 3;
            for (int j = 4; j <= i; j+=2)
            {
                dp[i] += 2 * dp[i-j];
            }
        }
        cout << dp[N] << endl;
    }

    return 0;
}
#endif