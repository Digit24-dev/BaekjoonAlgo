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
#define HOLE 'O'

int N, M; // 세로, 가로
char map[MAX][MAX];

int ans = INT32_MAX;

// L, R, U, D
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};

// R, B 구슬 추적
CORD red;
CORD blue;

void input()
{
    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> map[i][j];
            if (map[i][j] == 'R') {
                red = make_pair(i, j);
                map[i][j] = '.';
            }
            else if (map[i][j] == 'B') {
                blue = make_pair(i, j);
                map[i][j] = '.';
            }
        }
    }
}

int reverseDir(int dir)
{
    if (dir == 0) return 1;
    else if (dir == 1) return 0;
    else if (dir == 2) return 3;
    else if (dir == 3) return 2;
}

void move_ball(int Rx, int Ry, int Bx, int By, int cnt, int dir)
{
    if (cnt >= ans) return;
    if (cnt > 10) return;

    bool red_flag = false;
    bool blue_flag = false;

    // 빨간 구슬 시뮬레이션
    int nRx = Rx + dx[dir];
    int nRy = Ry + dy[dir];
    while (1)
    {
        if (map[nRx][nRy] == WALL) break;
        if (map[nRx][nRy] == HOLE) {
            red_flag = true;
            break;
        }
        nRx += dx[dir];
        nRy += dy[dir];
    }
    nRx -= dx[dir];
    nRy -= dy[dir];

    // 파란 구슬 시뮬레이션
    int nBx = Bx + dx[dir];
    int nBy = By + dy[dir];
    while (1)
    {
        if (map[nBx][nBy] == WALL) break;
        if (map[nBx][nBy] == HOLE) {
            blue_flag = true;
            break;
        }
        nBx += dx[dir];
        nBy += dy[dir];
    }
    nBx -= dx[dir];
    nBy -= dy[dir];

    if (blue_flag) return;
    else {
        if (red_flag) {
            ans = min(ans, cnt);
            return;
        }
    }
    
    // 같은 방향으로 움직여서 위치가 같아진 경우,
    // 더 많이 움직인 구슬을 하나 빼준다.
    if (nRx == nBx && nRy == nBy) {
        int red_dist = abs(Rx - nRx) + abs(Ry - nRy);
        int blue_dist = abs(Bx - nBx) + abs(By - nBy);

        if (red_dist > blue_dist){
            nRx -= dx[dir];
            nRy -= dy[dir];
        }else {
            nBx -= dx[dir];
            nBy -= dy[dir];
        }
    }

    for (size_t i = 0; i < 4; i++)
    {
        if (i == dir) continue;
        // 역방향
        if (i == reverseDir(dir)) continue;

        move_ball(nRx, nRy, nBx, nBy, cnt + 1, i);
    }
}

int solution()
{
    for (size_t i = 0; i < 4; i++)
    {
        move_ball(red.first, red.second, blue.first, blue.second, 1, i);
    }
    
    if (ans > 10 || ans == INT32_MAX) ans = -1;
    cout << ans;
}

int main()
{
    FASTIO

    input();

    // debug();

    solution();

    return 0;
}