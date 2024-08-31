#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int Floor, Start, Go, Up, Down;
int map[1000001];
bool visited[1000001];

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(0);

    cin >> Floor >> Start >> Go >> Up >> Down;
    
    if (Start == Go) {
        cout << 0 << endl;
        return 0;
    }

    queue<pair<int, int>> q;
    q.push(make_pair(Start, 0));
    visited[Start] = true;

    while (!q.empty())
    {
        pair<int, int> cur = q.front(); q.pop();
        int cnt = ++cur.second;
        int up = cur.first + Up;
        int down = cur.first - Down;

        if (up == Go || down == Go) {
            map[Go] = cnt;
            break;
        }

        if (up <= Floor && !visited[up]) {
            q.push(make_pair(up, cnt));
            visited[up] = true;
            map[up] = cnt;
        }
        if (down >= 1 && !visited[down]) {
            q.push(make_pair(down, cnt));
            visited[down] = true;
            map[down] = cnt;
        }
    }

    if (map[Go] == 0)
        cout << "use the stairs" << endl;
    else
        cout << map[Go] << endl;
    
    return 0;
}