#include <iostream>
#include <vector>

using namespace std;

int ans = 0;
int N, M;
bool visited[100] = {false, };

void dfs(int index, int sum, int cnt, vector<int> &arr)
{
    if (cnt == 3) {
        ans = max(ans, sum);

        return;
    }

    for (size_t i = index; i < N; i++)
    {
        if (!visited[i] && sum + arr[i] <= M) 
        {
            visited[i] = true;
            dfs(i + 1, sum + arr[i], cnt + 1, arr);
            visited[i] = false;
        }
    }
}

int main()
{
    cin >> N >> M;

    vector<int> bucket;
    bucket.resize(N);

    for (size_t i = 0; i < N; i++)
        cin >> bucket[i];

    dfs(0, 0, 0, bucket);

    cout << ans << endl;

    return 0;
}

