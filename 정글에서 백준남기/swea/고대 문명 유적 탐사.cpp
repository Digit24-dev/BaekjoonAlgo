#include <iostream>
#include <queue>
#include <algorithm>
#include <memory>
using namespace std;

int map[5][5];
bool visited[5][5];
int treasure[301];
int t_pointer = 0;
int M, K;

int ri[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
int rj[8] = {-1, 0, 1, 1, 1, 0, -1, -1};

int di[4] = { 0, 0, 1, -1 };
int dj[4] = { 1, -1, 0, 0 };

void debug(int cmap[5][5])
{
    for (size_t i = 0; i < 5; i++)
    {
        for (size_t j = 0; j < 5; j++)
        {
            cout << cmap[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void input() 
{
    cin >> K >> M;

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cin >> map[i][j];
        }
    }
    for (int i = 0; i < M; i++)
    {
        cin >> treasure[i];
    }
}

void rotate(int i, int j, int cmap[5][5], int cnt)
{
    queue<int> temp_q;

    for (size_t k = 0; k < cnt; k++)
    {
        for (int dir = 0; dir < 8; dir++)
        {
            temp_q.push(cmap[i + ri[dir]][j + rj[dir]]);
        }

        for (int dir = 2; dir < 8; dir++)
        {
            cmap[i + ri[dir]][j + rj[dir]] = temp_q.front(); temp_q.pop();
        }
        for (int dir = 0; dir < 2; dir++)
        {
            cmap[i + ri[dir]][j + rj[dir]] = temp_q.front(); temp_q.pop();
        }
    }
}

int bfs(int i, int j, int cmap[5][5])
{
    int ret = 0;
    queue<pair<int, int>> q, trace;

    q.push(make_pair(i, j));
    trace.push({ i,j });
    visited[i][j] = true;

    while (!q.empty())
    {
        pair<int, int> cur = q.front(); q.pop();


        for (size_t dir = 0; dir < 4; dir++)
        {
            int ni = cur.first + di[dir];
            int nj = cur.second + dj[dir];

            if (!visited[ni][nj] && ni >= 0 && ni < 5 && nj >= 0 && nj < 5 && cmap[i][j] == cmap[ni][nj])
            {
                visited[ni][nj] = true;
                q.push({ ni,nj });
                trace.push({ ni,nj });
            }
        }
    }

    if (trace.size() >= 3)
    {
        ret += trace.size();
        while (!trace.empty())
        {
            cmap[trace.front().first][trace.front().second] = 0;
            trace.pop();
        }
    }
    
    return ret;
}

int acquire(int cmap[5][5])
{
    int ret = 0;
    memset(visited, 0, sizeof(visited));

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (visited[i][j]) continue;
            int temp = 0;
            temp = bfs(i, j, cmap);

            if (temp > 2) {
                ret += temp;
            }
        }
    }

    return ret;
}

void explore()
{
    int ret = 0;
    int simulate[5][5];
    int max_map[5][5];
    int unit_max = 0;

    while (K--)
    {
        unit_max = 0;
        int cc = 1;
        // 탐사 진행
        for (int k = 1; k <= 3; k++)
        {
            for (int j = 1; j < 4; j++)
            {
                for (int i = 1; i < 4; i++)
                {
                    memcpy(simulate, map, sizeof(map));
                    rotate(i, j, simulate, k);
                    int score = acquire(simulate);

                    if (unit_max < score)
                    {
                        unit_max = score;
                        memcpy(max_map, simulate, sizeof(max_map));
                    }
                }
            }
        }
        //cout << "debug:: " << unit_max << endl;
        if (unit_max == 0)
            break;

        // 채우기
        while (true)
        {
            // 열 작은순, 행 큰순
            for (int j = 0; j < 5; j++)
            {
                for (int i = 5 - 1; i >= 0; i--)
                {
                    if (max_map[i][j] == 0) {
                        max_map[i][j] = treasure[t_pointer++];
                    }
                }
            }
            int newScore = 0;
            newScore = acquire(max_map);
            if (newScore == 0) break;
            unit_max += newScore;
        }
        
        memcpy(map, max_map, sizeof(map));

        cout << unit_max << " ";
    }
}

void solution()
{
    explore();
}

int main() {
    // 여기에 코드를 작성해주세요.

    input();

    solution();


    return 0;
}