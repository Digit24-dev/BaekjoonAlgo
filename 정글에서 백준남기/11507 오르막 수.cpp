#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>

#define FASTIO  cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
#define endl '\n'

using namespace std;

int main() {
    FASTIO

    int n;
    unsigned long bucket[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    cin >> n;
    
    while(--n)
    {
        for (int i = 0; i < 9; i++)
        {
            bucket[i + 1] += bucket[i] % 10007;
        }
    }
    
    cout << bucket[9] % 10007 << endl;

    return 0;
}