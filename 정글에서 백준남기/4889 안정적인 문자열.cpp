#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>

#define FASTIO  cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
#define endl '\n'

using namespace std;


int main()
{
    string line;
    int cnt = 1;
    int ans = 0;

    cin >> line;
    while (line != "-")
    {

        cout << cnt << ". " << ans << endl;
        cin >> line;
    }
    
    return 0;
}