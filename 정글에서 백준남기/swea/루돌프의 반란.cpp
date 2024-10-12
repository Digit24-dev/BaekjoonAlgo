#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
#include <string>
#include <iomanip>
using namespace std;

/*
    (1) 구성
    - N * N 격자, r(i) , c (j) : (1,1)부터 시작
    - M개의 턴, 루돌프 이동 후 산타 1번부터P까지
    - 거리 : 1-2 + 1-2 제곱
    
    (2) 루돌프 움직임
    - 가까운 산타 향해 1칸 돌진
    - r좌표 큰 산타 우선, c 좌표 큰 산타
    - 8방향 돌진 가능
    - 인접 대각선 방향도 1칸 전진

    (3) 산타 움직임
    - 1 ~ P 순서 움직임
    - 기절, 탈락 산타는 움직x
    - 루돌프에게 거리가 가까워지는 방향
    - 다른 산타 중첩x
    - 움직일 곳 없으면 정지
    - 루돌프에게 가까워질 수 있는 방법 없으면 움직 x
    - 산타는 4방향 이동, 상우하좌 순서로 이동

    (4) 충돌
    - 산타 == 루돌프
    - 루돌프가 움직여서 충돌시 산타 C, 루돌프 이동 방향으로 C밀려남
    - 산타가 움직여서 충돌시 D, 산타 이동 반대 방향으로 D밀려남
    - 밀리는 도중 충돌 x
    - board 밖이면 탈락
    - 밀린 칸에 산타 시 상호작용

    (5) 상호작용
    - 충돌 착지시 다른 산타 있으면 그 산타는 해당 방향으로 1칸 밀려남
    - 연쇄 작용, 보드 밖으로 나갈 시 탈락

    (6) 기절
    - 루돌프와 충돌 후 기절, k -> k+1 까지 기절
    - 충돌, 상호작용은 가능
    - 루돌프는 기절한 산타 선택 가능

    (7) 종료
    - M번의 턴에 걸쳐 이동 후 종료
    - P 모두 탈락시 종료
    - 매 턴 산타는 1점 추가

    각 산타가 얻은 최종 점수 출력
*/
#define CORD pair<int, int>
void collision(bool rudolf, int santaIdx);
int calc(CORD a, CORD b);
void debug(string line);

struct status
{
    bool alive = true;
    bool stun = false;
    int id;
    int dist;
    int stunTime = 0;
    int dir;
    int score = 0;
    CORD pos;
};

int N, M, P, C, D; // 판 크기, 턴 수, 산타수(1~30), 루돌프 (1~N), 산타힘(1~N)
int map[51][51];

CORD rudolf;
int rudolf_dir;

status santas[31];

int ri[8] = {1, 1, 1, 0, 0, -1, -1, -1};
int rj[8] = {1, 0, -1, 1, -1, 1, 0, -1};

int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};

bool isRanged(int i, int j)
{
    return i > 0 && i <= N && j > 0 && j <= N;
}

void input()
{
    cin >> N >> M >> P >> C >> D;
    int a, b, c;
    cin >> a >> b;
    rudolf = { a,b };

    for (int i = 0; i < P; i++)
    {
        cin >> a >> b >> c;
        santas[a].pos = make_pair(b, c);
        santas[a].id = a;
    }
    
    // render on map
    map[rudolf.first][rudolf.second] = -1;
    for (int i = 1; i <= P; i++)
    {
        map[santas[i].pos.first][santas[i].pos.second] = i;
    }
}

void moveRudolf()
{
    int foundedSanta = 0;
   /* queue<CORD> q;
    q.push(rudolf);
    int visited[51][51];
    memset(visited, 0, sizeof(visited));
    visited[rudolf.first][rudolf.second] = 0;
    int f_dist = 10000;
    vector<status> ab;

    while (!q.empty())
    {
        auto cur = q.front(); q.pop();

        if (f_dist < visited[cur.first][cur.second])
            break;

        if (map[cur.first][cur.second] > 0 && visited[cur.first][cur.second] < f_dist)
        {
            
            ab.push_back(santas[map[cur.first][cur.second]]);
            f_dist = visited[cur.first][cur.second];
        }

        for (size_t dir = 0; dir < 8; dir++)
        {
            int ni = cur.first + ri[dir];
            int nj = cur.second + rj[dir];

            if (isRanged(ni, nj) && visited[ni][nj] == 0) {
                visited[ni][nj] += visited[cur.first][cur.second] + 1;
                q.push({ ni,nj });
            }
        }
    }*/

    vector<status> ss;
    int minDist = 10000;
    for(int i=1; i<=P; i++)
    {
        auto& e = santas[i];

        if (!e.alive) 
            continue;
        
        // 대각선 거리 1로 무마
        int dist = calc(e.pos, rudolf);
        // 두 좌표 차이 중 최댓값?
        // int dist = max(abs(e.pos.first - rudolf.first), abs(e.pos.second - rudolf.second));

        e.dist = dist;
        if (dist <= minDist) {
            ss.push_back(e);
            minDist = dist;
        }
    }
    
    sort(ss.begin(), ss.end(), [](status a, status b) {
        if (a.dist == b.dist) {
            if (a.pos.first == b.pos.first) return a.pos.second > b.pos.second;
            return a.pos.first > b.pos.first;
        }
        return a.dist < b.dist;
    });
    
    foundedSanta = ss[0].id;

    if (foundedSanta == 0)
        return;

    int minDir;
    minDist = 10000;
    CORD minMove;

    for (size_t dir = 0; dir < 8; dir++)
    {
        int ni = rudolf.first + ri[dir];
        int nj = rudolf.second + rj[dir];

        if (isRanged(ni, nj))
        {
            int dist = calc({ ni,nj }, santas[foundedSanta].pos);
            if (dist < minDist)
            {
                minDist = dist;
                minDir = dir;
                minMove = { ni,nj };
            }
        }
    }
    rudolf_dir = minDir;
    map[rudolf.first][rudolf.second] = 0;
    rudolf = minMove;

    if (map[minMove.first][minMove.second] > 0)
        collision(true, map[minMove.first][minMove.second]);

    map[minMove.first][minMove.second] = -1;
}

int calc(CORD a, CORD b)
{
    return int(pow(abs(a.first - b.first), 2) + pow(abs(a.second - b.second), 2));
}

void moveSanta()
{
    for (int idx = 1; idx <= P; idx++)
    {
        // 기절 | 탈락
        if (!santas[idx].alive || santas[idx].stun)
            continue;

        CORD s_cord = santas[idx].pos;
        CORD minMove = { -1, -1 }; 
        int minDir = -1;
        int minDist = calc(s_cord, rudolf);

        for (size_t dir = 0; dir < 4; dir++)
        {
            int ni = s_cord.first + di[dir];
            int nj = s_cord.second + dj[dir];
            int dist = calc({ ni,nj }, rudolf);

            // 격자 내, 다른 산타가 없고 현재 위치보다 가까운 거리의 위치가 있을 경우
            if (isRanged(ni, nj) && map[ni][nj] <= 0 && minDist > dist)
            {
                minDist = dist;
                minMove = { ni,nj };
                minDir = dir;
            }
        }

        // 움직이지 않는 경우
        if (minMove.first == -1)
            continue;

        map[santas[idx].pos.first][santas[idx].pos.second] = 0;
        santas[idx].dir = minDir;
        
        // 충돌과 상호작용
        if (map[minMove.first][minMove.second] == -1) {
            collision(false, idx);
            continue;
        }

        santas[idx].pos = minMove;
        map[minMove.first][minMove.second] = idx;
    }
}

int inverseDir(int dir)
{
    switch (dir)
    {
    case 0:
        return 2;
        break;
    case 1:
        return 3;
        break;
    case 2:
        return 0;
        break;
    case 3:
        return 1;
        break;
    }
}

bool interactiveTrueOrDead(int idx1, int idx2, bool rudolf, int dir)
{
    if (rudolf)
    {
        int ti = santas[idx2].pos.first + ri[dir];
        int tj = santas[idx2].pos.second + rj[dir];
        
        if (!isRanged(ti, tj)) {
            santas[idx2].alive = false;
            map[santas[idx2].pos.first][santas[idx2].pos.second] = 0;
            return false;
        }
        else if(map[ti][tj] > 0)
            interactiveTrueOrDead(idx2, map[ti][tj], rudolf, dir);
        
        map[ti][tj] = idx2;
        santas[idx2].pos = { ti, tj };

        return true;
    }
    else
    {
        int ti = santas[idx2].pos.first + di[dir];
        int tj = santas[idx2].pos.second + dj[dir];

        if (!isRanged(ti, tj)) {
            santas[idx2].alive = false;
            map[santas[idx2].pos.first][santas[idx2].pos.second] = 0;
            return false;
        }
        else if (map[ti][tj] > 0)
            interactiveTrueOrDead(idx2, map[ti][tj], rudolf, dir);
        
        map[ti][tj] = idx2;
        santas[idx2].pos = { ti, tj };

        return true;
    }
}

void collision(bool rudolf, int santaIdx)
{
    if (rudolf)
    {
        int ti = santas[santaIdx].pos.first + ri[rudolf_dir] * C;
        int tj = santas[santaIdx].pos.second + rj[rudolf_dir] * C;
        santas[santaIdx].stun = true;
        santas[santaIdx].stunTime = M;

        if (!isRanged(ti, tj))
        {
            santas[santaIdx].alive = false;
            map[santas[santaIdx].pos.first][santas[santaIdx].pos.second] = 0;
            return;
        }
        else if (map[ti][tj] > 0)
        {
            // 상호작용
            interactiveTrueOrDead(santaIdx, map[ti][tj], rudolf, rudolf_dir);
        }
        //map[santas[santaIdx].pos.first][santas[santaIdx].pos.second] = 0;
        santas[santaIdx].pos = { ti, tj };
        map[ti][tj] = santaIdx;
        santas[santaIdx].score += C;
    }
    else
    {
        // 상우하좌
        int ti = santas[santaIdx].pos.first + di[santas[santaIdx].dir] + di[inverseDir(santas[santaIdx].dir)] * D;
        int tj = santas[santaIdx].pos.second + dj[santas[santaIdx].dir] + dj[inverseDir(santas[santaIdx].dir)] * D;
        santas[santaIdx].stun = true;
        santas[santaIdx].stunTime = M;

        if (!isRanged(ti, tj))
        {
            santas[santaIdx].alive = false;
            map[santas[santaIdx].pos.first][santas[santaIdx].pos.second] = 0;
            return;
        }
        else if (map[ti][tj] > 0)
        {
            // 상호작용
            interactiveTrueOrDead(santaIdx, map[ti][tj], rudolf, inverseDir(santas[santaIdx].dir));
        }
        //map[santas[santaIdx].pos.first][santas[santaIdx].pos.second] = 0;
        santas[santaIdx].pos = { ti, tj };
        map[ti][tj] = santaIdx;
        santas[santaIdx].score += D;
    }
}

void updateStun()
{
    for(int i=1; i<=P; i++)
    {
        auto& e = santas[i];
        if (e.alive && e.stunTime - M >= 2)
            e.stun = false;
    }
}

bool updateSocre()
{
    bool ret = false;
    for (int i = 1; i <= P; i++)
    {
        auto& e = santas[i];
        if (e.alive) {
            e.score++;
            ret = true;
        }
    }
    return ret;
}

void debug(string line)
{
    cout << "=====" << M << "=====" << line << endl;
    for (size_t i = 1; i <= N; i++)
    {
        for (size_t j = 1; j <= N; j++)
        {
            if (map[i][j] == -1)
                cout << setw(2) << '*' << " ";
            else
                if (map[i][j] != 0 && santas[map[i][j]].stun)
                    cout << setw(2) << map[i][j] << "!";
                else
                    cout << setw(2) << map[i][j] << " ";
        }
        cout << endl;
    }
    //cout << "=====" << " " << "=====" << endl;
}

int main() {
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);

    input();

    //debug("처음");

    while (M--)
    {
        updateStun();

        moveRudolf();

        // debug("루돌프 이동");

        moveSanta();

        // debug("산타 이동");

        if (!updateSocre())
            break;
    }
    //debug("");

    for (int i = 1; i <= P; i++)
    {
        cout << santas[i].score << " ";
    }

    return 0;
}