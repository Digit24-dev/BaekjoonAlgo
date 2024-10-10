#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <iomanip>
using namespace std;

#define INF 987654
#define MAX_N 2001

int m,n;
int start = 0;

struct travel
{
    int id;
    int revenue;
    int dest;
    int profit;
    
    // bool operator<(const travel& other) const {
    //     if (profit == other.profit) return id > other.id;
    //     return profit < other.profit;
    // };

    struct Comparator {
        bool operator()(const travel& a, const travel& b) const {
            if (a.profit == b.profit) {
                return a.id > b.id;
            }
            return a.profit < b.profit;
        }
    };
};

bool isMade[30001];
bool isCanceled[30001];
vector<int> dist;
// vector<vector<pair<int, int>>> graph;
// vector<pair<int, int>> graph[20001];
int graph[MAX_N][MAX_N];
// priority_queue<travel> tours;
priority_queue<travel, vector<travel>, travel::Comparator> tours;

void dijkstra()
{
    vector<bool> visited(n, false);
    for(int i=0; i<n; ++i)
        dist[i] = INF;
    dist[start] = 0;
    for (int i = 0; i < n-1; i++)
    {
        int v=0, minDist = INF;
        for (int j = 0; j < n; j++)
        {
            if (!visited[j] && minDist > dist[j]) {
                v = j;
                minDist = dist[j];
            }
        }
        visited[v] = true;
        for (int j = 0; j < n; j++)
        {
            if (!visited[j] && dist[v] != INF && graph[v][j] != INF && dist[j] > dist[v] + graph[v][j])
                dist[j] = dist[v] + graph[v][j];
        }        
    }
}

// void dijkstra2()
// {
//     for(int i=0; i<n; ++i)
//         dist[i] = INF;

//     priority_queue<pair<int, int>> pq;
//     vector<bool> visited(n, false);
//     dist[start] = 0;
//     visited[start] = true;
//     pq.push({0, start});

//     while(!pq.empty())
//     {
//         int cost = -pq.top().first;
//         int dest = pq.top().second;
//         pq.pop();
        
//         if (cost > dist[dest]) continue;

//         for(auto& edge : graph[dest])
//         {
//             int next = edge.first;
//             int weight = edge.second;
            
//             if (dist[next] > weight + dist[dest])
//             {
//                 dist[next] = weight + dist[dest];
//                 pq.push({ dist[next], next });
//             }
//         }
//     }
// }

void construct()
{
    cin >> n >> m;
    dist.resize(n);
    // graph.resize(n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            graph[i][j] = INF;
        }
        graph[i][i] = 0;
    }
    
    for (size_t i = 0; i < m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u][v] = min(graph[u][v], w);
        graph[v][u] = min(graph[v][u], w);
        // graph[u].push_back({v, w});
        // graph[v].push_back({u, w});
    }
}

void addProducts(int id, int revenue, int dest)
{
    travel temp;
    temp.id = id;
    temp.dest = dest;
    temp.revenue = revenue;
    temp.profit = revenue - dist[dest];
    isMade[id] = true;

    tours.push(temp);
}

void removeProduct(int id)
{
    if (isMade[id]) isCanceled[id] = true;
}

void changeStart()
{
    cin >> start;
    dijkstra();

    vector<travel> travels;
    while (!tours.empty())
    {
        travels.push_back(tours.top());
        tours.pop();
    }
    for(travel t: travels)
    {
        addProducts(t.id, t.revenue, t.dest);
    }
}

int sellProduct()
{
    while (!tours.empty())
    {
        travel _t = tours.top();
        if (_t.profit < 0)
            break;
        tours.pop();
        if (!isCanceled[_t.id])
            return _t.id;
    }
    return -1;
}

int main()
{
    FILE* fp;
    freopen_s(&fp, "input (4).txt", "r", stdin);

    int code, Q;
    int id, revenue, dest;
    cin >> Q;
    for (int order = 0; order < Q; order++)
    {
        cin >> code;
        switch (code)
        {
        case 100:
            construct();
            dijkstra();
            break;
        case 200:
            cin >> id >> revenue >> dest;
            addProducts(id, revenue, dest);
            break;
        case 300:
            int id;
            cin >> id;
            removeProduct(id);
            break;
        case 400:
            cout << sellProduct() << endl;
            break;
        case 500:
            changeStart();
            break;
        }
    }
}