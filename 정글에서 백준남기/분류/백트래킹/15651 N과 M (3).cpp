#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>

#define FASTIO  cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
#define endl '\n'

using namespace std;

int N, M;
int arr[8];

void dfs(vector<int> &bucket, int depth, int idx)
{
    if (depth == M) {
        for(auto e: bucket)
            cout << e << " ";
        cout << endl;
        return;
    }

    for (int i = 1; i <= N; i++)
    {
        bucket.push_back(i);
        dfs(bucket, depth + 1, i);
        bucket.pop_back();
    }
}

int main()
{
    FASTIO
    
    cin >> N >> M;
    
    vector<int> bucket;
    dfs(bucket, 0, 1);

    return 0;
}