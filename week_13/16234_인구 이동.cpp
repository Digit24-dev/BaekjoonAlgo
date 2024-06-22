#include <iostream>
#include <vector>
#include <queue>

#define MAX_N   50
#define MAX_R   100

#define endl    '\n'

using namespace std;

int di[4] = {1, -1, 0, 0};
int dj[4] = {0, 0, 1, -1};

int N, L, R;
int map[MAX_N + 1][MAX_N + 1];
bool open[MAX_N+1][MAX_N+1];

vector<pair<int, int>> work_q;
int ans = 0;

void debug_map()
{
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < N; j++)
        {
            cout << map[i][j] << " ";
        }
        cout << endl;
    }
}

void debug_o()
{
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < N; j++)
        {
            cout << open[i][j] << " ";
        }
        cout << endl;
    }
}


void input()
{
    cin >> N >> L >> R;
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < N; j++)
        {
            cin >> map[i][j];
        }
    }
}

void search()
{
    // 완탐
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < N; j++)
        {
            if (L <= map[i][j] && map[i][j] <= R)
                open[i][j] = true;
        }
    }
}

void simulation(int x, int y)
{
    // search
    int sum = 0;
    int cnt = 0;
    
    queue<pair<int, int>> q;
    vector<pair<int, int>> work;
    q.push(make_pair(x , y));

    while (!q.empty())
    {
        auto cur = q.front(); q.pop();
        int i = cur.first;
        int j = cur.second;

        for (int dir = 0; dir < 4; dir++)
        {
            int ni = i + di[dir];
            int nj = j + dj[dir];

            if (open[ni][nj]) {
                cnt++;
                sum += map[ni][nj];
                open[ni][nj] = false;
                work.push_back(make_pair(ni, nj));
            }
        }
    }

    // update
    for (auto elem : work)
        map[elem.first][elem.second] = sum / cnt;
}

bool flag;
void solution()
{

    // simulation
    while (1)
    {
        flag = false;
        
        // bfs();
        search();

        debug_o();

        // simulation
        for (size_t i = 0; i < N; i++)
        {
            for (size_t j = 0; j < N; j++)
            {
                if (open[i][j]) {
                    simulation(i, j);
                }
            }
        }

        debug_map();

        if (!flag)
            break;

        ans++;
    }
    
    cout << ans << endl;
}

int main()
{
    input();

    solution();

    return 0;
}