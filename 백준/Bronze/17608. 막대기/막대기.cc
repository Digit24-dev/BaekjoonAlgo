#include <iostream>
#include <stack>

#define MAX 100000

using namespace std;

int main() {
    int n;
    int arr[MAX];
    stack<int> s;

    cin >> n;

    for (size_t i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    
    s.push(arr[n - 1]);
    for (int i = n - 2; i >= 0; i--)
    {
        if (arr[i] > s.top())
            s.push(arr[i]);
    }
    
    cout << s.size() << endl;

    return 0;
}