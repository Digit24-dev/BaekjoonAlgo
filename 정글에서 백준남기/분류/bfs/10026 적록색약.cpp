#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>

#define FASTIO  cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
#define endl '\n'

#define pii pair<int, int>

int N;
using namespace std;
int grid[101][101];
bool visited[101][101];
bool visited2[101][101];

int di[] = {1, -1, 0, 0};
int dj[] = {0, 0, 1, -1};

bool isRange(int i, int j)
{
    return i >= 0 && i < N && j >= 0 && j < N;
}

void bfs(int i, int j)
{
    int cur_color = grid[i][j];
    queue<pii> q;
    q.push({i,j});
    visited[i][j] = true;
    while (!q.empty())
    {
        pii current = q.front(); q.pop();
        
        for (int dir = 0; dir < 4; dir++)
        {
            int ni = current.first + di[dir];
            int nj = current.second + dj[dir];

            if (isRange(ni, nj) && !visited[ni][nj] && grid[ni][nj] == cur_color)
            {
                q.push({ni, nj});
                visited[ni][nj] = true;
            }
        }
    }
}

void bfs_rg(int i, int j)
{
    int cur_color = grid[i][j];
    bool flag_rg = false;
    if (cur_color != 'B')
        flag_rg = true;

    queue<pii> q;
    q.push({i,j});
    visited2[i][j] = true;
    while (!q.empty())
    {
        pii current = q.front(); q.pop();
        
        for (int dir = 0; dir < 4; dir++)
        {
            int ni = current.first + di[dir];
            int nj = current.second + dj[dir];

            if (!flag_rg) {
                if (isRange(ni, nj) && !visited2[ni][nj] && grid[ni][nj] == cur_color)
                {
                    q.push({ni, nj});
                    visited2[ni][nj] = true;
                }
            }
            else {
                if (isRange(ni, nj) && !visited2[ni][nj] && grid[ni][nj] != 'B')
                {
                    q.push({ni, nj});
                    visited2[ni][nj] = true;
                }
            }
        }
    }
}

int main() {
    FASTIO
    
    string line;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> line;
        for (int j = 0; j < N; j++)
        {
            grid[i][j] = line[j];
        }
    }
    
    // normal person
    int normal = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (!visited[i][j]) {
                ++normal;
                bfs(i, j);
            }
        }
    }

    int rg = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (!visited2[i][j]) {
                ++rg;
                bfs_rg(i, j);
            }
        }
    }
    
    cout << normal << " " << rg << endl;

    return 0;
}