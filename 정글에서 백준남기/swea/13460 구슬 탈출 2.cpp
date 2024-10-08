#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <memory.h>

using namespace std;

#define CORD pair<int, int>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);

#define MAX 10 + 1

#define WALL '#'
#define BALNK '.'
#define HOLE 'O'
#define RED 'R'
#define BLUE 'B'

int N, M; // 세로, 가로
char map[MAX][MAX];
char simul[MAX][MAX];
bool visited[MAX][MAX];

// L, R, U, D
int dx[4] = {0, 0, -1, 1};
int dj[4] = {1, -1, 0, 0};

// R, B 구슬 추적
CORD red;
CORD blue;

void input()
{
    cin >> N >> M;
    string line;
    for (size_t i = 0; i < N; i++)
    {
        cin >> line;

        for (size_t j = 0; j < M; j++)
        {
            map[i][j] = line[j];
            if (line[j] == RED) red = make_pair(i, j);
            if (line[j] == BLUE) blue = make_pair(i, j);
        }
    }
}

void debug_v()
{
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < M; j++)
        {
            cout << visited[i][j];
        }
        cout << endl;
    }
}

void debug()
{
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < M; j++)
        {
            cout << map[i][j];
        }
        cout << endl;
    }
}

void move(int dir)
{
    // 해당 방향으로의 i or j 값이 더 낮은 구슬 부터 선택
    bool rob = false; // 0: red , 1: blue
    switch (dir)
    {
    case 0: // L
        rob = red.second < blue.second ? 0 : 1;
        break;
    case 1: // R
        rob = red.second > blue.second ? 0 : 1;
        break;
    case 2: // U
        rob = red.first > blue.first ? 0 : 1;
        break;
    case 3: // D
        rob = red.first < blue.first ? 0: 1;
        break;
    }

    if (rob)
    {
        int ni = dx[dir];
        int nj = dj[dir];
        while (map[ni][nj] != WALL)
        {
            ni += dx[dir]; 
            nj += dj[dir];
        }
        red = make_pair(ni, nj);
    }
    else
    {
        
    }
}

vector<int> route;

struct myStruct
{
    CORD cord;
    int times = 0;
    vector<int> routes;
};

myStruct simulationRED()
{
    myStruct ret;
    queue<myStruct> q; q.push({red, 0, });
    bool endFlag = false;

    while (!q.empty())
    {
        myStruct cur = q.front(); q.pop();
        cout << cur.cord.first << ", " << cur.cord.second << endl;
        cout << cur.routes.size() << endl;

        if (cur.routes.size() >= 11) break;

        for (size_t dir = 0; dir < 4; dir++)
        {
            int ni = cur.cord.first + dx[dir];
            int nj = cur.cord.second + dj[dir];

            if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue;

            if (map[ni][nj] != WALL && !visited[ni][nj]) 
            {
                while (map[ni][nj] != WALL)
                {
                    if (map[ni][nj] == HOLE){
                        endFlag = true;
                        break;
                    }
                    visited[ni][nj] = true;
                    ni += dx[dir];
                    nj += dj[dir];
                }
                if (endFlag) {
                    ret.cord = cur.cord;
                    vector<int> _t(cur.routes.begin(), cur.routes.end());
                    _t.push_back(dir);
                    ret.routes = _t;
                    goto end;
                }

                myStruct enq;
                vector<int> _t(cur.routes.begin(), cur.routes.end());
                _t.push_back(dir);
                enq.routes = _t;
                enq.cord = make_pair(ni - dx[dir], nj - dj[dir]);

                q.push(enq);
            }
        }
    }

end:
    debug_v();

    return ret;
}

void simulationBLUE(vector<int> routes)
{
    for (auto route : routes)
    {
        
    }
}

int solution()
{
    myStruct ret = simulationRED();
    cout << "ANS: " << ret.routes.size() << endl;
}

int main()
{
    FASTIO

    input();

    // debug();

    solution();

    return 0;
}
