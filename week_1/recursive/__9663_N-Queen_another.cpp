#include <iostream>
#include <cstring>

using namespace std;

int N;

int board[15][15];
int res= 0;
bool check(int r, int c) {
    int t = min(r,c);
    for(int i=1;i<=t;i++) {
        if(board[r-i][c-i] == 1) return false;
    }
    t = min(r, N-c);
    for(int i=1;i<=t;i++) {
        if(board[r-i][c+i] == 1) return false;
    }
    for(int i =0;i<N;i++) {
        if(board[i][c] == 1) return false;
    }
    return true;
}

void solve(int d) {
    if (d == N) {
        res++;
        return;
    }

    for(int i =0;i<N;i++) {
        if(!check(d, i)) continue;
        board[d][i] = 1;
        solve(d+1);
        board[d][i] = 0;
    }

}


int main() {
    cin >> N;
    memset(board, 0, sizeof(board));
    solve(0);
    cout << res;
    return 0;
}