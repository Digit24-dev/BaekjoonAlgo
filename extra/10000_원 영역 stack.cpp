#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

#define endl '\n'

using namespace std;

// bool check_outside(pair<int, int> r1, pair<int, int> r2)
// {
//     return r1.first + r1.second < r2.first - r2.second || r1.first - r1.second > r2.first + r2.second;
// }

// bool check_inside(pair<int, int> r1, pair<int, int> r2)
// {
//     return r1.first - r1.second > r2.first - r2.second && r1.first + r1.second < r2.first + r2.second;
// }

// bool check_boarder(pair<int, int> r1, pair<int, int> r2)
// {
//     return r1.first - r1.second == r2.first - r2.second && r1.first + r1.second < r2.first + r2.second
//         || r1.first - r1.second > r2.first - r2.second && r1.first + r1.second == r2.first + r2.second;
// }

int main() {

    int n, x, r;
    int ans = 1;
    int total_width, width;
    // 0: L / 1: R
    vector<pair<int, int>> circles;
    stack<pair<int, int>> st;

    cin >> n;

    while (n--)
    {
        cin >> x >> r;
        circles.push_back(make_pair(0, x - r));
        circles.push_back(make_pair(1, x + r));
    }

    // x 기준 오름차순 정렬
    sort(circles.begin(), circles.end(), [](pair<int, int> a, pair<int, int> b) {
        if (a.second == b.second) return a.first > b.first;
        return a.second < b.second;
    });

    for (size_t i = 0; i < circles.size(); i++)
    {
        if (circles[i].first == 0) {
            st.push(circles[i]);
            continue;
        }
        
        total_width = 0;

        while (!st.empty())
        {
            pair<int, int> cur = st.top(); st.pop();

            if (cur.first == 0) {
                width = circles[i].second - cur.second;
                
                if (total_width == width)
                    ans += 2;
                else
                    ++ans;
                
                st.push(make_pair(2, width));
                break;
            }
            else if (cur.first == 2)
                total_width += cur.second;
        }
    }

    cout << ans << endl;

    return 0;
}