#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>

#define FASTIO  cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);

using namespace std;

int N, M;
int arr[9];

void dfs(int depth, int idx, int arr[])
{
    if (depth == M) {
        for (int i = 1; i <= N; i++)
        {
            if (arr[i])
                cout << i << " ";
        }
        cout << endl;
        return;
    }

    for (int i = idx + 1; i <= N; i++)
    {
        arr[i] = 1;
        dfs(depth + 1, i, arr);
        arr[i] = 0;
    }
}

int main()
{
    FASTIO
    
    cin >> N >> M;
    
    dfs(0, 0, arr);

    return 0;
}