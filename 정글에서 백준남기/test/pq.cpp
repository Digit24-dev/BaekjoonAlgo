#include <queue>
#include <iostream>
using namespace std;

int main()
{
    priority_queue<int> pq;
    pq.push(1);
    pq.push(2);
    pq.push(3);
    pq.push(4);
    pq.push(5);

    cout << pq.top() << endl;

    return 0;

}