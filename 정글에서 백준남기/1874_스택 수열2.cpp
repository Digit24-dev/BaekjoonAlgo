#include <iostream>
#include <stack>
#include <string>

#define endl          '\n'

using namespace std;

int main()
{
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n, cnt = 1;
    cin >> n;

    stack<int> s;
    string ans;

    while (n--)
    {
        int x;
        cin >> x;

        while (cnt <= x)
        {
            s.push(cnt++);
            ans += '+\n';
        }
        
        if (s.top() != x)
        {
            cout << "NO\n";
            return 0;
        }
        s.pop();
        ans += "-\n";
    }
    cout << ans;

    return 0;
}