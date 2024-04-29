#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

#define endl '\n'

using namespace std;

bool check_outside(pair<int, int> r1, pair<int, int> r2)
{
    return r1.first + r1.second < r2.first - r2.second || r1.first - r1.second > r2.first + r2.second;
}

bool check_inside(pair<int, int> r1, pair<int, int> r2)
{
    return r1.first - r1.second > r2.first - r2.second && r1.first + r1.second < r2.first + r2.second;
}

bool check_boarder(pair<int, int> r1, pair<int, int> r2)
{
    return r1.first - r1.second == r2.first - r2.second && r1.first + r1.second < r2.first + r2.second 
        || r1.first - r1.second > r2.first - r2.second && r1.first + r1.second == r2.first + r2.second;
}

// 실패
int main() {

    int n, x, r;
    int ans = 0;
    vector<pair<int, int>> circles;
    stack<pair<int, int>> st;

    cin >> n;

    while (n--)
    {
        cin >> x >> r;
        circles.push_back(make_pair(x, r));
    }
    
    // r 기준 오름차순 정렬
    sort(circles.begin(), circles.end(), [](pair<int, int> a, pair<int, int> b) {
        if (a.second == b.second) return a.first < b.first;
        return a.second < b.second;
    });

    // 반지름 기준 정렬된 원 부터 그린다.
    for (size_t i = 0; i < circles.size(); i++)
    {
        cout << circles[i].first << ", " << circles[i].second << endl;
        // 자기 자신의 영역 그림.
        ++ans;
        
        // 비어 있으면 현재 값 푸시
        if (st.empty()) {
            st.push(circles[i]);
            continue;
        }
        
        if (circles[i].second == st.top().second) {
            while (!st.empty())
                st.pop();
            ++ans;
        }
        else if (st.top().second == circles[i].first || st.top().first == circles[i].first){
            if (circles[i].first == st.top().first)
                st.push(circles[i]);
        }
        else {
            while (!st.empty())
                st.pop();
        }
    }

    cout << ans + 1 << endl;

    return 0;
}