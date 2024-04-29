#include <iostream>
#include <queue>

using namespace std;

int main(){

    int n, index = 1;
    queue<int> q;

    cin >> n;

    for (size_t i = 1; i <= n; i++)
        q.push(i);

    while (q.size() > 1)
    {
        q.pop();
        int cur = q.front(); q.pop();
        q.push(cur);
    }
    
    cout << q.front() << endl;

    return 0;
}