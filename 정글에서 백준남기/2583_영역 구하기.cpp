#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

#define MAX 101
#define cord pair<int, int>

int M, N, K;    // N: 가로, j, x // M: 세로, i, y
int map[MAX][MAX];
bool visited[MAX][MAX];

int ans1 = 0;
vector<int> ans2;

int di[4] = {1, -1, 0, 0};
int dj[4] = {0, 0, 1, -1};

vector<pair<CORD, CORD>> sq;

void debug()
{
    cout << "====" << endl;
    for(int i=0; i<M; i++) {
        for(int j=0; j<N; j++) {
            cout << map[i][j] << " ";
        }
        cout << endl;
    }
    cout << "====" << endl;
}

void input()
{
    cin >> M >> N >> K;
    for (int i=0; i<K; i++) 
    {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        
        for (int i=x1; i<x2; i++) {
            for (int j=y1; j<y2; j++) {
                map[j][i] += 1;
            }
        }
    }
}

void bfs(int i, int j) 
{
    int area = 0;

    queue<CORD> q;
    q.push(make_pair(i, j));
    visited[i][j] = true;

    while (!q.empty())
    {
        CORD cur = q.front(); q.pop();
        area++;

        for(int dir=0; dir < 4; dir++) 
        {
            int ni = cur.first + di[dir];
            int nj = cur.second + dj[dir];

            if (!visited[ni][nj] && ni >= 0 && ni < M && nj >= 0 && nj < N && !map[ni][nj])
            {
                visited[ni][nj] = true;
                q.push(make_pair(ni, nj));
            }
        }
    }

    ans2.push_back(area);
}

void solution() 
{
    for(int i=0; i<M; i++) {
        for(int j=0; j<N; j++) {
            if (!map[i][j] && !visited[i][j]) {
                ans1++;
                bfs(i, j);
            }
        }
    }
}

int main()
{
    input();

    solution();

    sort(ans2.begin(), ans2.end());

    cout << ans1 << endl;
    for (int e : ans2)
        cout << e << " ";

    return 0;
}