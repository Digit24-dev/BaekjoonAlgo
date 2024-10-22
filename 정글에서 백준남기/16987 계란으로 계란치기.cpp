#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>

#define FASTIO  cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);

using namespace std;

int N;
int ans = 0;

struct Egg
{
    int S;
    int W;
};

vector<Egg> eggs;

void simulate(int idx)
{
    if (idx == N) {
        int sum = 0;
        for (int i = 0; i < N; i++)
        {
            if (eggs[i].S <= 0) ++sum;
        }
        ans = max(ans, sum);
        return;
    }

    // collision
    Egg *sel = &eggs[idx];
    if (sel->S <= 0) 
        simulate(idx + 1);

    Egg *pSel;
    bool flag = false;

    // next
    for (int i = 0; i < N; i++)
    {
        if (i == idx) continue;
        
        pSel = &eggs[i];
        
        if (eggs[i].S > 0) {
            pSel->S -= sel->W;
            sel->S -= pSel->W;

            flag = true;
            simulate(idx+1);

            pSel->S += sel->W;
            sel->S += pSel->W;
        }
    }

    if (!flag) simulate(N);
}

int main()
{
    cin >> N;
    eggs.resize(N);
    for (int i = 0; i < N; i++)
        cin >> eggs[i].S >> eggs[i].W;
    
    simulate(0);

    cout << ans << endl;
    
    return 0;
}