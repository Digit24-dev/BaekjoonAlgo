#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <memory.h>

using namespace std;

#define cord pair<int, int>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);

#define MAX 100 + 1

int main()
{
    FASTIO

    int x, y;
    int n;    
    
    cin >> y >> x;
    cin >> n;

    vector<int> w = {0, x};
    vector<int> h = {0, y};

    for (size_t i = 0; i < n; i++)
    {
        int dir, num;
        cin >> dir >> num;
        
        if (dir == 1)
            h.push_back(num);
        else
            w.push_back(num);
    }
    
    sort(h.begin(), h.end());
    sort(w.begin(), w.end());

    int max_w = 0, max_h = 0;
    for (size_t i = 0; i < h.size() - 1; i++)
    {
        int _temp = h[i+1] - h[i];
        if (_temp > max_h) 
            max_h = _temp;
    }
    for (size_t i = 0; i < w.size() - 1; i++)
    {
        int _temp = w[i+1] - w[i];
        if (_temp > max_w) 
            max_w = _temp;
    }

    cout << max_w * max_h << endl;

    return 0;
}