#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <memory.h>

using namespace std;

#define cord pair<int, int>

int ans[6];
int arr[14];
int k;

void dfs(int depth, int idx)
{
    if (depth == 6) {
        for (size_t i = 0; i < 6; i++)
            cout << ans[i] << " ";
        cout << endl;
        return;
    }

    for (size_t i = idx; i < k; i++)
    {
        ans[depth] = arr[i];
        dfs(depth + 1, i + 1);
    }
}

int main()
{
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);

    cin >> k;

    while (k != 0)
    {
        for (size_t i = 0; i < k; i++)
            cin >> arr[i];

        dfs(0, 0);

        cout << endl;
        cin >> k;
    }


    return 0;
}