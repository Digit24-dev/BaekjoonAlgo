#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

#define pi pair<int, int>

#define endl '\n'

using namespace std;

int n, d;
int ans = 0;

vector<pi> temp;

void input()
{
    cin >> n;
    temp.reserve(n);
    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        if (a < b)
            temp.push_back(make_pair(a, b));
        else
            temp.push_back(make_pair(b, a));
    }
    cin >> d;
}

void solution()
{
    priority_queue<int, vector<int>, greater<int>> pq;

    sort(temp.begin(), temp.end(), [](pi a, pi b){
        if (a.second == b.second) return a.first < b.first;
        return a.second < b.second;
    });

    for (int i = 0; i < temp.size(); i++)
    {
        if (temp[i].second - temp[i].first > d) continue;

        int start = temp[i].first;
        int end  = temp[i].second;
        
        pq.push(start);

        while (!pq.empty()) {
            if (end - d > pq.top())
                pq.pop();
            else {
                ans = max(ans, (int)pq.size());
                break;
            }
        }
    }
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);

    input();

    solution();

    cout << ans << endl;

    return 0;
}