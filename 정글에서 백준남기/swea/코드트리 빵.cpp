#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

#define MAX_N 15 + 1
#define MAX_M min(N*N, 30)

int N, M;
int map[MAX_N][MAX_N];

int di[4] = { -1, 0, 0, 1 };
int dj[4] = { 0, -1, 1, 0 };

int distCheck(pair<int, int> from, pair<int, int> to);

inline bool isRanged(int i, int j)
{
    return i >= 0 && i < N && j >= 0 && j < N;
}

struct info
{
    pair<int, int> togo;
    pair<int, int> pos;
    bool start = false;
    bool arrived = false;

    void searchBaseCamp()
    {
        start = true;
        queue<pair<int, int>> q;
        vector<vector<bool>> visited(N, vector<bool>(N, false));
        q.push(togo);
        visited[togo.first][togo.second] = true;
        vector<pair<int, int>> baseCamps;
        int founded_dist = 10000;

        while (!q.empty())
        {
            pair<int, int> cur = q.front(); q.pop();
            
            if (map[cur.first][cur.second] == 1)
            {
                int ret = distCheck(cur, togo);
                if (ret > founded_dist)
                    continue;

                founded_dist = ret;

                baseCamps.push_back({ cur.first, cur.second });
            }

            for (int dir = 0; dir < 4; dir++)
            {
                int ni = cur.first + di[dir];
                int nj = cur.second + dj[dir];

                if (isRanged(ni, nj) && !visited[ni][nj] && map[ni][nj] != 2)
                {
                    q.push({ ni, nj });
                    visited[ni][nj] = true;
                }
            }
        }

        sort(baseCamps.begin(), baseCamps.end(), [](pair<int, int> a, pair<int, int> b) {
            if (a.first == b.first) return a.second < b.second;
            return a.first < b.first;
        });

        pos.first = baseCamps[0].first;
        pos.second = baseCamps[0].second;
        map[pos.first][pos.second] = 2;
    }
};
vector<info> people;

void input()
{
    cin >> N >> M;
    people.resize(M);
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> map[i][j];
        }
    }
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        people[i].togo = make_pair(a - 1, b - 1);
    }
}

int distCheck(pair<int, int> from, pair<int, int> to)
{
    return abs(to.first - from.first) + abs(to.second - from.second);
}

void moveAll()
{
    for (int i = 0; i < people.size(); i++)
    {
        info person = people[i];
        if (person.start && !person.arrived)
        {
            // 최단경로 탐색 후 이동
            // 최단경로 :: distance가 최소이지 않을까?
            pair<int, int> minDist = { 10000, 0 };
            
            for (int dir = 0; dir < 4; dir++)
            {
                int ni = person.pos.first + di[dir];
                int nj = person.pos.second + dj[dir];

                if (!isRanged(ni, nj) || map[ni][nj] == 2) continue;

                int ret = distCheck({ ni, nj }, person.togo);
                
                if (minDist.first > ret)
                    minDist = make_pair(ret, dir);
            }

            // minDist로 고고싱
            people[i].pos.first += di[minDist.second];
            people[i].pos.second += dj[minDist.second];
        }
    }
}

void stop()
{
    for (auto& e : people)
    {
        if (!e.arrived && e.start && e.pos.first == e.togo.first && e.pos.second == e.togo.second)
        {
            e.arrived = true;
            map[e.pos.first][e.pos.second] = 2;
            //cout << "도착한 사람~ :" << e.togo.first << ", " << e.togo.second << endl;
        }
    }
}

void solution()
{
    int T = 0;
    bool flag;

    while (true)
    {
        ++T;
        flag = false;

        // (1) 모두 움직여~
        moveAll();

        // (2) 도착한 사람 멈춰~
        stop();

        // (3) T번째 사람 출발~
        if (T <= M)
            people[T - 1].searchBaseCamp();

        // (4) 모두 도착했는지 확인
        for (auto& e : people)
        {
            if (!e.arrived)
                flag = true;
        }

        if (!flag)
            break;
    }
    cout << T << endl;
}

int main() {
    cin.tie(0); ios::sync_with_stdio(0);

    input();

    solution();

    return 0;
}