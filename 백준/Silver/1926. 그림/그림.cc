#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MAX_N 501
#define endl '\n'

int map[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N];

int m,n;
int pic_cnt = 0;
int max_depth = 0;

int di[4] = {1, -1, 0, 0};
int dj[4] = {0, 0, 1, -1};

void bfs(int i, int j){
    int temp_depth = 0;

    queue<pair<int, int>> q;
    q.push(make_pair(i, j));
    visited[i][j] = true;

    while (!q.empty())
    {
        auto cur = q.front(); q.pop();
        ++temp_depth;

        for (size_t dir = 0; dir < 4; dir++)
        {
            int ni = cur.first + di[dir];
            int nj = cur.second + dj[dir];

            if (!visited[ni][nj] && map[ni][nj] == 1){
                visited[ni][nj] = true;
                q.push(make_pair(ni, nj));
            }
        }
    }
    max_depth = max(max_depth, temp_depth);
}

void input()
{
    for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < m; j++)
        {
            cin >> map[i][j];
        }
    }
}

void debug()
{
    for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < m; j++)
        {
            cout << visited[i][j] << " ";
        }
        cout << endl;
    }
    
}

int main() {

    cin >> n >> m;

    input();

    for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < m; j++)
        {
            if (!visited[i][j] && map[i][j] == 1)
            {
                ++pic_cnt;
                bfs(i, j);
            }
        }
    }

    // debug();

    cout << pic_cnt << endl;
    cout << max_depth << endl;

    return 0;
}