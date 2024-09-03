#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <memory.h>

using namespace std;

#define cord pair<int, int>

int map[20][20];

// 1 2 3 4 6 7 8 9
int di[4] = {-1, 0, 1, 1};
int dj[4] = {1, 1, 0, 1};

int ri[4] = {1, 0, -1, -1};
int rj[4] = {-1, -1, 0, -1};

inline bool isRange(int i, int j)
{
    return i >= 1 && i< 20 && j >= 1 && j < 20;
}

bool checkWinner(int i, int j)
{
    int BorW = map[i][j];

    for (size_t dir = 0; dir < 4; dir++)
    {
        int cnt = 1;

        int ni = i + di[dir];
        int nj = j + dj[dir];
        int tri = i + ri[dir];
        int trj = j + rj[dir];

        if (isRange(tri, trj) && map[tri][trj] == BorW)
            continue;

        if (!(isRange(ni, nj) && map[ni][nj] == BorW)) 
            continue;

        ++cnt;

        for (size_t k = 0; k < 6; k++)
        {
            ni += di[dir];
            nj += dj[dir];

            if (isRange(ni, nj) && map[ni][nj] == BorW)
                ++cnt;
            else
                break;
        }
        
        if (cnt == 5)
            return true;
    }

    return false;
}

int main()
{
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);

    // input
    for (size_t i = 1; i <= 19; i++)
    {
        for (size_t j = 1; j <= 19; j++)
        {
            cin >> map[i][j];
        }
    }

    bool endFlag = false;
    
    // solve
    for (size_t j = 1; j <= 19; j++)
    {
        for (size_t i = 1; i <= 19; i++)
        {
            // cout << i << " " << j << endl;
            // 처음부터 탐색
            if (map[i][j] != 0 && checkWinner(i, j))
            {
                cout << map[i][j] << endl;
                cout << i << " " << j << endl;
                endFlag = true;
                goto end;
            }
        }
    }

end:
    if (!endFlag) 
    {
        cout << 0 << endl;
    }

    return 0;
}