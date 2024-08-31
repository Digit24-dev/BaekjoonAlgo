#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>

#define FASTIO ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define MAXN 101

using namespace std;

int n, m;
int graph[MAXN][MAXN];
const int maximum = 1073741823;

void debug()
{
    cout << "DEBUG" << endl;
    for (size_t i = 1; i <= n; i++)
    {
        for (size_t j = 1; j <= n; j++)
        {
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }
    cout << "END DEBUG" << endl;
}

void input() 
{
    // Read input
    cin >> n >> m;
    for (size_t i = 1; i <= n; i++)
    {
        for (size_t j = 1; j <= n; j++)
        {
            graph[i][j] = maximum;
        }
    }

    for (size_t i = 0; i < m; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;

        // a -> b 로 가는 비용 c
        graph[a][b] = min(graph[a][b], c);
    }
}

void solution()
{
    // Floyd-Warshall Algorithm
    for (size_t k = 1; k <= n; k++) 
    {
        for (size_t i = 1; i <= n; i++)
        {
            for (size_t j = 1; j <= n; j++) 
            {
                if (i == j)
                    continue;
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }
}

void output()
{
    for (size_t i = 1; i <= n; i++)
    {
        for (size_t j = 1; j <= n; j++)
        {
            if (graph[i][j] == maximum)
                cout << "0 ";
            else
                cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    FASTIO;

    // Read input
    input();

    // Process input
    solution();

    // Output result
    output();

    return 0;
}