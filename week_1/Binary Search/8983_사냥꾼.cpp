#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>

#define endl '\n'

using namespace std;

int M, N, L;
int pic_cnt = 0;
int mid;

vector<int> camp;
vector<pair<int, int>> animals;

void DEBUG() {
    for (int i = 0; i < N; i++)
    {
        cout << animals[i].first << ", " << animals[i].second << endl;
    }
}

int main() {

    cin.tie(0); ios_base::sync_with_stdio(0);

    // input
    cin >> M >> N >> L;
    camp.resize(M);
    animals.resize(N);

    // camp
    for (size_t i = 0; i < M; i++)
        cin >> camp[i];
    
    // animals
    for (int i = 0; i < N; i++)
    {
        int x, y;
        cin >> x >> y;
        animals[i] = make_pair(x, y);
    }

    DEBUG();

    // LOGIC

    // SORT
    sort(camp.begin(), camp.end());

    mid = camp[camp.size() >> 1];

    sort(animals.begin(), animals.end(), [](auto a, auto b) {
        return abs(mid - a.first) + a.second < abs(mid - b.first) + b.second;
    });
    
    cout << mid << endl;
    DEBUG();

    // SEARCH

    /*
    1. 캠프를 오름차순 정렬
    2. 사냥감을 정렬
    3. 
    */

    return 0;
}
