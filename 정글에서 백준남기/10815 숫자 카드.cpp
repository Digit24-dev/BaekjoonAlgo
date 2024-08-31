#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int N, M;
vector<int> has;

void bsearch(int X) {
    int l = 0, r = N - 1;

    while (l <= r)
    {
        int mid = (l + r) / 2;

        if (X < has[mid]) {
            r = mid - 1;
        } else if ( X > has[mid]) {
            l = mid + 1;
        } else {
            cout << "1 ";
            return;
        }
    }

    cout << "0 ";
    return;
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(0);

    cin >> N;
    has.resize(N);

    for (size_t i = 0; i < N; i++)
    {
        cin >> has[i];
    }

    sort(has.begin(), has.end());
    
    cin >> M;
    for (size_t i = 0; i < M; i++)
    {
        int temp;
        cin >> temp;
        bsearch(temp);
    }
    
    return 0;
}