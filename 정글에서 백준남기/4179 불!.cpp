#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <memory.h>

using namespace std;
#define CORD pair<int, int>

int R, C;
int board[1000][1000];
int fires[1000][1000];
bool visited[1000][1000];

queue<CORD> fq;
CORD start;

int ans = 0;
int di[4] = {1,-1,0,0};
int dj[4] = {0,0,1,-1};

inline bool isRange(int i, int j)
{
    return i >= 0 && i < R && j >= 0 && j < C;
}

void input()
{
    cin >> R >> C;
    for (int i = 0; i < R; i++)
    {
        string line;
        cin >> line;
        for (int j = 0; j < C; j++)
        {
            board[i][j] = line[j];
            if (board[i][j] == 'J')
                start = {i,j};
            else if (board[i][j] == 'F')
                fq.push({i,j});
        }
    }
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (board[i][j] == 'F')
            {
                fires[i][j] = 0;
            }
            else if (board[i][j] != '#')
                fires[i][j] = 2001;
        }
    }
}

void debug()
{
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            cout << setw(3) << fires[i][j] << " ";
        }
        cout << endl;
    }
}

void bfsFire(int i, int j)
{
    // 맵에 불의 전파 속도 맵을 표시한 후 지훈이가 갈 수 있는 여부 판단하자.
    while (!fq.empty())
    {
        auto cur = fq.front(); fq.pop();
        
        for (int dir = 0; dir < 4; dir++)
        {
            int ni = cur.first + di[dir];
            int nj = cur.second + dj[dir];

            if (isRange(ni, nj) && board[ni][nj] != '#' && fires[ni][nj] == 2001)
            {
                fq.push({ni,nj});
                fires[ni][nj] = fires[cur.first][cur.second] + 1;
            }
        }
    }
}

void bfs(int i, int j)
{
    queue<pair<int, CORD>> q;
    q.push(make_pair(0, start));
    visited[start.first][start.second] = true;
    
    while (!q.empty())
    {
        auto cur = q.front(); q.pop();
        int score = cur.first;
        CORD pos = cur.second;
        
        for (int dir = 0; dir < 4; dir++)
        {
            int ni = pos.first + di[dir];
            int nj = pos.second + dj[dir];
            
            if (isRange(ni, nj) && board[ni][nj] != '#' && !visited[ni][nj] && score + 1 < fires[ni][nj])
            {
                q.push(make_pair(score + 1, make_pair(ni, nj)));
                visited[ni][nj] = true;
            }
            else if (!isRange(ni, nj))
            {
                cout << score + 1 << endl;
                return;
            }
        }
    }
    cout << "IMPOSSIBLE" << endl;
    return;
}

int main()
{
    cin.tie(0); ios::sync_with_stdio(0);
    
    input();
    
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (board[i][j] == 'F')
                bfsFire(i, j);
        }
    }
    
    bfs (start.first, start.second);

    return 0;
}
