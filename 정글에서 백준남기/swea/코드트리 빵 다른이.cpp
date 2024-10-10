/*
    2022년 하반기 오후 1번 문제 - 코드트리 빵
    빵을 구하고자 하는 사람이 m명 있는데 1번 사람은 1분에, 2번 사람은 2분에, m번 사람은 m분에 편의점으로 이동
    *출발 시간 전에는 겪자 밖, 목표로하는 편의점은모두 다르다. 이 모든 일은 n*n 크기의격자 위에서 진행.

    빵을 구하는 사람들의 행동 
    1. 격자에 있는 사람들 모두 본인이 편의점 방향으로 1칸 이동.
        최단거리로 움직이고 상왼우하 우선 순위로 이동
        *최단 거리 : 도달하기까지 거쳐야 하는 칸의 수의 최소
    2. 편의점에 도착하면 해당 편의점에서 멈추게 되고, 그 칸은 Block -> Block 시점은 사람들이 모두 이동한 후

    3. 현재 시간이 t <= m
    t번 사람은 자신이 가고 싶은 편의점과 가장 가까운 베이스 캠프로 들어감. * 최단거리
    행이 작은, 열이 작은 우선순위
    이때부터 다른 사람들은 해당 베이스 캠프에 지나갈 수 없다. 이때부터 계속 Block

    사람들이 다 이동하고 -> 마감된 편의점 Block -> 베이스캠프 Block

    Return : 총 몇 분 후에 모두 편의점에 도착하는지를 구하는 프로그램을 작성


    문제 설계 : 
    베이스 캠프의 위치 -> map[][];
    편의점의 위치 -> map[][]; 
    --> map을 통해서 이동 가능한지 check해두기

    int t = 0;
    while(!checkAllDone()){

    }



    입력
    격자 크기 : 2 <= n <= 15
    사람의 수 : 1 <= m <= min(n^2, 30);
    베이스 캠프의 수 : m <= 베이스 캠프의 수 <= n^2 - m

*/
#include<iostream>
#include<vector>
#include<queue>

using namespace std;

struct Player{
    int crow;
    int ccol;
    int grow;
    int gcol;
};

int n, m;
int map[16][16] = {0};
int drow[4] = {-1, 0, 0, 1};
int dcol[4] = {0, -1, 1, 0};

vector<Player> v;

int t = 0;
void init(){
    cin >> n >> m;
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) cin >> map[i][j];
    for(int i = 0; i < m; i++){
        int row; int col;
        cin >> row >> col;
        v.push_back({-1,-1,row-1,col-1});
    }
}

void move(int idx){
    // 이미 나간 사람이면 움직일 필요 X
    if(v[idx].crow == v[idx].grow && v[idx].ccol == v[idx].gcol) return;

    // grow, gcol 에서 bfs를 한다.
    int visited[16][16] = {0};
    queue<pair<int,int>> q;
    visited[v[idx].grow][v[idx].gcol] = 1;
    q.push({v[idx].grow, v[idx].gcol});
    while(!q.empty()){
        pair<int,int> temp = q.front(); q.pop();
        for(int i = 0; i < 4; i++){
            int nrow = temp.first + drow[i];
            int ncol = temp.second + dcol[i];
            if(nrow < 0 || ncol < 0 || nrow + 1 > n || ncol + 1 > n) continue;
            if(visited[nrow][ncol] != 0) continue;
            if(map[nrow][ncol]==-1) continue;
            q.push({nrow,ncol});
            visited[nrow][ncol] = visited[temp.first][temp.second]+1;
        }
    }
    // cout << idx << "의 최단거리 visited 배열 \n";
    // for(int i = 0; i < n; i++){
    //     for(int j = 0; j < n; j++){
    //         cout << visited[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    // 상 왼 우 하로 돌려서 최소가 되는 칸
    // 최소가 되는 칸을 어떻게 구하지? 최솟값과 그때의 방향을 저장해둔다.
    // 여러개면 우선 순위대로 
    int min_dist = 1e9;
    int min_d = -1;
    for(int i = 0; i < 4; i++){
        int nrow = v[idx].crow + drow[i];
        int ncol = v[idx].ccol + dcol[i];
        if(nrow < 0 || ncol < 0 || nrow + 1 > n || ncol + 1 > n) continue;
        if(map[nrow][ncol]==-1) continue;
        if(visited[nrow][ncol] == 0) continue;
        if(min_dist > visited[nrow][ncol]) {min_dist = visited[nrow][ncol]; min_d = i;}
    }
    
    // 그리고 이동 v 벡터를 update해줘야 한다. 
    v[idx].crow = v[idx].crow + drow[min_d];
    v[idx].ccol = v[idx].ccol + dcol[min_d];
}
void moveAll(){
    for(int i = 0; i < min(t,m); i++){
        move(i);
    }
}
void checkDone(){
    for(int i = 0; i < min(t,m); i++){
        //만약 현재 위치랑 goal 위치랑 같으면 그 위치를 -1로 막아버리기
        if(v[i].crow == v[i].grow && v[i].ccol == v[i].gcol) map[v[i].crow][v[i].ccol] = -1;
    }
}
void insertBase(int idx){
    // grow, gcol에서 bfs를 한다음에
    int visited[16][16] = {0};
    queue<pair<int,int>> q;
    visited[v[idx].grow][v[idx].gcol] = 1;
    q.push({v[idx].grow, v[idx].gcol});
    while(!q.empty()){
        pair<int,int> temp = q.front(); q.pop();
        for(int i = 0; i < 4; i++){
            int nrow = temp.first + drow[i];
            int ncol = temp.second + dcol[i];
            if(nrow < 0 || ncol < 0 || nrow + 1 > n || ncol + 1 > n) continue;
            if(visited[nrow][ncol] != 0) continue;
            if(map[nrow][ncol]==-1) continue;
            q.push({nrow,ncol});
            visited[nrow][ncol] = visited[temp.first][temp.second]+1;
        }
    }

    // 이중 포문 돌면서 가능한 베이스 캠프를 찾는다.
    // 그리고 최솟값 찾기
    int min_dist = 1e9;
    int base_row = -1;
    int base_col = -1;
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++){
        if(map[i][j] == 1 && visited[i][j] != 0 && visited[i][j] < min_dist){
            min_dist = visited[i][j];
            base_row = i;
            base_col = j;
        }
    }
    map[base_row][base_col] = -1;
    v[idx].crow = base_row;
    v[idx].ccol = base_col;
    // 그리고 베이스캠프 -1로 바꾸기
}
bool checkAllDone(){
    for(int i = 0; i < m; i++){
        if(v[i].crow != v[i].grow || v[i].ccol != v[i].gcol) return false; 
    }   
    return true;
}
void macro(){
    while(1){
        moveAll();
        checkDone();
        if(t<=m-1){
            insertBase(t);
        }
        if(checkAllDone()) return;
        t++;
    }
}
int main(){
    init();
    macro();
    cout << t + 1 << "\n";
}