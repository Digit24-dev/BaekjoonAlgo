#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define MAX_N   10001

int n, m;
int start, dest;
vector<vector<pair<int, int>>> graph;
vector<vector<pair<int, int>>> b_graph;
vector<int> indegree;

vector<int> result;
vector<bool> visited;

void input()
{
    cin >> n >> m;
    graph.resize(n + 1);
    b_graph.resize(n + 1);

    indegree.reserve(n + 1);
    for (size_t i = 1; i <= n; i++)
    {
        indegree[i] = 0;
    }
    
    visited.resize(n + 1, false);
    result.resize(n + 1, 0);

    for (size_t i = 0; i < m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        
        graph[u].push_back(make_pair(v, w));
        b_graph[v].push_back(make_pair(u, w));
        ++indegree[v];
    }
    
    cin >> start >> dest;
}

void debug()
{
    for (size_t i = 1; i <= m; i++)
    {
        for (size_t j = 0; j < graph[i].size(); j++)
        {
            cout << i << " -> " << graph[i][j].first << " : " << graph[i][j].second << endl;
        }
    }
}

int solution()
{
    queue<int> q;
    /* topology sort */
    q.push(start);
    while (!q.empty())
    {
        int cur = q.front(); q.pop();
        for (auto elem : graph[cur])
        {
            int d = elem.first;
            int w = elem.second;

            indegree[d]--;
            result[d] = max(result[d], result[cur] + w);
            if (indegree[d] == 0)
                q.push(d);
        }
    }
    /* backtracking for answer */
    int cnt = 0;
    q.push(dest);
    while (!q.empty())
    {
        int cur = q.front(); q.pop();
        for (auto elem : b_graph[cur])
        {
            int d = elem.first;
            int w = elem.second;

            if (result[cur] - result[d] == w) {
                cnt++;
                if (!visited[d]) {
                    q.push(d);
                    visited[d] = true;
                }
            }
        }
    }
    return cnt;
}

int main() {

    cin.tie(0); cout.tie(0);
    ios_base::sync_with_stdio(0);

    input();

    // debug();

    int ans = solution();

    cout << result[dest] << endl;
    cout << ans << endl;

    return 0;
}
