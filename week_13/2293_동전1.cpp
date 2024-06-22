#include <iostream>
#include <vector>

using namespace std;

#define MAXN    100
#define MAXK    10000

int dp[MAXN][MAXK];

int main()
{
    int n, k;
    vector<int> coins;
    cin >> n >> k;
    coins.resize(n);

    for (size_t i = 0; i < n; i++)
    {
        cin >> coins[i];
    }

    
}