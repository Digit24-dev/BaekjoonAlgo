#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <iomanip>
using namespace std;

#define DIJKSTRA 1
#define INF 987654

#if DIJKSTRA
vector<vector<pair<int, int>>> graph;
vector<int> dist;
bool isChanged = true;
#else
vector<pair<int, int>> graph[2001];
int f_graph[2001][2001];
//int f_graph[2001][2001];
#endif

struct travel {
    int id;
    int revenue;
    int dest;
};

int Q;
int m, n;
int start = 0;

map<int, travel> productsHash;

#if DIJKSTRA
int dijkstra(int destination)
{
    if (!isChanged)
        return dist[destination];

    // 다익스트라
    priority_queue<pair<int, int>> pq;
    vector<bool> visited(n, false);
    dist[start] = 0;
    visited[start] = true;

    pq.push({ 0, start });
    while (!pq.empty())
    {
        int cost = -pq.top().first;
        int current = pq.top().second;
        pq.pop();

        if (cost > dist[current])
            continue;

        for (auto& edge : graph[current]) 
        {
            int next = edge.first;
            int weight = edge.second;

            if (dist[current] + weight < dist[next]) {
                dist[next] = dist[current] + weight;
                pq.push({ dist[next], next });
            }
        }

        //for (unsigned int i = 0; i < graph[current].size(); i++)
        //{
        //    int next = graph[current][i].first;
        //    int weight = graph[current][i].second;

        //    //cout << "|| next: " << next << "| weight: " << weight << endl;

        //    if (weight + dist[current] < dist[next])
        //    {
        //        dist[next] = weight + dist[current];
        //        pq.push({ -dist[next], next });
        //    }
        //}
    }
    isChanged = false;

    if (dist[destination] == INF)
        return -1;
    return dist[destination];
}
#else
void floyd()
{
    //memset(f_graph, INF, sizeof(f_graph));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == j) f_graph[i][j] = 0;
        }
    }

    for (int k = 0; k < n; k++)
        for (int i =0 ; i < n; i++)
            for (int j = 0; j < n; j++)
                f_graph[i][j] = min(f_graph[i][j], f_graph[i][k] + f_graph[k][j]);

    //debugAll();
}
#endif

void construct()
{
#ifndef DIJKSTRA
    memset(f_graph, INF, sizeof(f_graph));
#endif // !DIJKSTRA
    
    cin >> n >> m;
    dist.resize(n);
    graph.resize(n);
    for (int i = 0; i < n; i++)
        dist[i] = INF;
    
    for (int i = 0; i < m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
#if DIJKSTRA
        graph[u].push_back({ v, w });
        graph[v].push_back({ u, w });
#else
        /*graph[u].push_back({ v, w });
        graph[v].push_back({ u, w });*/
        f_graph[u][v] = min(f_graph[u][v], w);
        f_graph[v][u] = min(f_graph[v][u], w);
#endif
    }
    //debugAll();
#ifndef DIJKSTRA
    floyd();
#endif // !DIJKSTRA
}

void addProducts()
{
    int id, revenue, dest;
    cin >> id >> revenue >> dest;
    productsHash[id] = { id, revenue, dest };
}

void removeProduct(int id)
{
    if (productsHash.find(id) != productsHash.end())
        productsHash.erase(id);
}

void sellProduct()
{
    priority_queue<pair<int, int>> ppq;

    map<int, travel>::iterator iter;
    for (iter = productsHash.begin(); iter != productsHash.end(); iter++)
    {
        travel info = (*iter).second;
#if DIJKSTRA
        int ret = dijkstra(info.dest);
#else
        int ret = f_graph[start][info.dest];
#endif
        cout << "debug:: id:" << info.id << "| revenue:" << info.revenue << " | cost:" << ret << " | dest:" << info.dest << endl;
        if (ret != -1 && info.revenue - ret >= 0)
        {
            ppq.push({ info.revenue - ret, -info.id });
        }
    }

    if (!ppq.empty())
    {
        cout << -ppq.top().second << endl;
        removeProduct(-ppq.top().second);
    }
    else
        cout << -1 << endl;
}

void changeStart()
{
    cin >> start;
#ifdef DIJKSTRA
    isChanged = true;
#else
    floyd();
#endif // DIJKSTRA
}

int main() {
    // 여기에 코드를 작성해주세요.
    /*FILE* fp;
    freopen_s(&fp, "input (4).txt", "r", stdin);*/

    int code;

    cin >> Q;
    for (int order = 0; order < Q; order++)
    {
        cin >> code;
        switch (code)
        {
        case 100:
            construct();
            break;
        case 200:
            addProducts();
            break;
        case 300:
            int id;
            cin >> id;
            removeProduct(id);
            break;
        case 400:
            sellProduct();
            break;
        case 500:
            changeStart();
            break;
        }
    }

    return 0;
}