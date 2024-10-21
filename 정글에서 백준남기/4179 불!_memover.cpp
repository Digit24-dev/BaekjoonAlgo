#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>

using namespace std;
#define CORD pair<int, int>

int R, C;
int board[1000][1000];
int visited[1000][1000];
CORD start;
queue<pair<int, CORD>> player;
queue<CORD> fires;
int ans = 0;
int di[4] = {1,-1,0,0};
int dj[4] = {0,0,1,-1};
bool endFlag = false;

bool isRange(int i, int j)
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
            {
                start = {i,j};
                player.push(make_pair(0, make_pair(i,j)));
            }
            else if (board[i][j] == 'F')
            {
                fires.push({i,j});
                visited[i][j] = -1;
            }
            else if (board[i][j] == '#')
            {
                visited[i][j] = -1;
            }
        }
    }
}

int movePlayer()
{
    int size = player.size();
    
    while (size--)
    {
        auto data = player.front(); player.pop();
        CORD cur = data.second;
        int score = data.first;
        
        if (visited[cur.first][cur.second] == -1) {
            continue;
        }

        for (int dir = 0; dir < 4; dir++)
        {
            int ni = cur.first + di[dir];
            int nj = cur.second + dj[dir];

            if (make_pair(ni,nj) == start)
                continue;

            if (isRange(ni, nj) && visited[ni][nj] == 0)
            {
                visited[ni][nj] = visited[cur.first][cur.second] + 1;
                player.push(make_pair(score + 1, make_pair(ni,nj)));
            }
            else if (!isRange(ni, nj))
            {
                return score + 1;
            }
        }
    }
    if (player.size() == 0)
        endFlag = true;
    return 0;
}

void moveFires()
{
    int size = fires.size();
    while (size--)
    {
        CORD cur = fires.front(); fires.pop();
        
        for (int dir = 0; dir < 4; dir++)
        {
            int ni = cur.first + di[dir];
            int nj = cur.second + dj[dir];

            if (isRange(ni, nj) && board[ni][nj] != '#')
            {
                fires.push({ni,nj});
                visited[ni][nj] = -1;
            }
        }
    }
}

void debug()
{
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            cout << setw(3) << visited[i][j] << " ";
        }
        cout << endl;
    }
    
}

void solution()
{
    while (!endFlag)
    {
        // debug();

        int ret = movePlayer();

        if (ret > 0) {
            cout << ret << endl;
            return;
        }

        moveFires();
    }
    cout << "IMPOSSIBLE" << endl;
    return;
}

int main()
{
    input();

    solution();

    return 0;
}
