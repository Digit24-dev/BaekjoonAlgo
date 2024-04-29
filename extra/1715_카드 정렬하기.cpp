#include <iostream>
#include <queue>

using namespace std;

int main() {

    priority_queue<int, vector<int>, greater<int>> pq;
    int N;
    int ans = 0;

    cin >> N;

    for (size_t i = 0; i < N; i++)
    {
        int temp;
        cin >> temp;
        pq.push(temp);
    }
    
    while (!pq.empty() && pq.size() > 1)
    {
        int first = pq.top();  pq.pop();
        int second = pq.top(); pq.pop();

        ans += first + second;
        pq.push(first + second);
    }

    cout << ans << endl;

    return 0;
}