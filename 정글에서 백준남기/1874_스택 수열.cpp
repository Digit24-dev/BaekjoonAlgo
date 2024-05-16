#include <iostream>
#include <stack>
#include <string>

#define endl          '\n'
#define print(dat)      (a[chr_idx++] = dat)

using namespace std;

int main()
{
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    char a[200001];
    int chr_idx = 0;
    int temp, n, maxv;

    cin >> n;
    maxv = n;
    stack<int> st;

    int idx = 1;
    while (n--)
    {
        cin >> temp;
        
        if (st.empty()) {
            
            do {
                st.push(idx);
                idx++;
                print('+');
            } while (temp > st.top());

            if (temp == st.top()) {
                st.pop();
                print('-');
            } else {
                cout << "NO" << endl;
                exit(0);
            }
        }
        else if (st.top() < temp) {
            do {
                st.push(idx);
                idx++;
                print('+');
            } while (temp > st.top() && idx <= maxv);

            if (temp == st.top()) {
                st.pop();
                print('-');
            } else {
                cout << "NO" << endl;
                exit(0);
            }
        }
        else if (st.top() > temp) {
            do {
                st.pop();
                print('-');
            } while (!st.empty() && temp < st.top());

            if (temp == st.top()) {
                st.pop();
                print('-');
            } else {
                cout << "NO" << endl;
                exit(0);
            }
        }
        else {
            st.pop();
            print('-');
        }
    }

    for (size_t i = 0; i < 2 * maxv; i++)
    {
        cout << a[i] << endl;
    }

    return 0;
}

