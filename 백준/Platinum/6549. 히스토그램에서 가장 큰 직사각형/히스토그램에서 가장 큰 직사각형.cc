#include <iostream>
#include <vector>
#include <stack>

#define MAX 100001

using namespace std;
vector<long long> squares;
int n;

int main() {
    cin.tie(NULL); cout.tie(NULL);
    ios_base::sync_with_stdio(0);
    
    squares.reserve(MAX);
    
    cin >> n;

    while (n)
    {
        for (size_t i = 0; i < n; i++)
            cin >> squares[i];
        
        long long ans = 0;
        stack<int> st;

        for (int i = 0; i < n; i++) {
            while (!st.empty() && squares[i] < squares[st.top()])
            {
                long long height, weight;

                height = st.top(); st.pop();

                if (st.empty())
                    weight = i;
                else
                    weight = i - st.top() - 1;

                ans = max(ans, (long long)(squares[height] * weight));
            }
            st.push(i);
        }

        while (!st.empty())
        {
            long long hTop = squares[st.top()];
            int I = n;
            st.pop();

            if (!st.empty())
                I = n - st.top() - 1;
            if (ans < I * hTop)
                ans = I * hTop;
        }
        
        cout << ans << endl;
        cin >> n;
    }

    return 0;
}