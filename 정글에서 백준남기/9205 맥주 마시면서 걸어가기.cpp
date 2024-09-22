#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <memory.h>

using namespace std;

#define cord pair<int, int>

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(0);

    int t, n;
    CORD start, end;
    bool visited[100];
    
    cin >> t;

    while (t--)
    {
        vector<CORD> conv;

        cin >> n;
        cin >> start.first >> start.second;

        conv.resize(n);
        for (size_t i = 0; i < n; i++)
        {
            cin >> conv[i].first >> conv[i].second;
        }
        cin >> end.first >> end.second;

        memset(visited, false, sizeof(visited));
        queue<CORD> q;
        bool flag = false;
        q.push(CORD(start.first, start.second));

        while (!q.empty())
        {
            CORD cur = q.front(); q.pop();
            
            if (abs(cur.first - end.first) + abs(cur.second - end.second) <= 1000) {
                flag = true;
                break;
            } else {
                for(int i=0; i<conv.size(); i++)
                {
                    auto elem = conv[i];
                    if (!visited[i] && (abs(cur.first - elem.first) + abs(cur.second - elem.second)) <= 1000) {
                        q.push(CORD(elem.first, elem.second));
                        visited[i] = true;
                    }
                }
            }
        }
        if (flag)
            cout << "happy" << endl;
        else
            cout << "sad" << endl;
    }

    return 0;
}