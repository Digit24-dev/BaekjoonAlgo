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

int main() {

    int n, x, r;
    int ans = 0;
    vector<pair<int, int>> circles;
    stack<pair<int, int>> st;
    stack<pair<int, int>> st_board;

    cin >> n;

    while (n--)
    {
        cin >> x >> r;
        circles.push_back(make_pair(x, r));
    }

    // x 기준 오름차순 정렬
    sort(circles.begin(), circles.end());

    for (size_t i = 0; i < circles.size(); i++)
    {
        // 스택이 비어있을 경우
        if (st.empty()) {
            st.push(circles[i]);
            continue;
        }

        auto top = st.top();

        // top의 오른쪽과 현재의 왼쪽이 겹칠 경우
        if (top.first + top.second == circles[i].first - circles[i].second) {
            st.push(circles[i]);
            continue;
        }

        // top의 왼쪽과 왼쪽이 겹칠 경우
        if (top.first - top.second == circles[i].first - circles[i].second) {
            //st.push(circles[i]);
            st_board.push(circles[i]);
            continue;
        }

        // board와 오른쪽이 겹칠 경우
        if (top.first + top.second == circles[i].first + circles[i].second) {
            // stack을 빼면서 왼쪽 비교하기
            while (!st.empty()) {
                st.pop(); ++ans;
            }
        }

        // 겹치지 않고 top 안 영역일 경우
        else if (top.first + top.second > circles[i].first + circles[i].second) {
            ++ans;
        }

        // 겹치지 않고 top의 밖 영역일 경우
        else {
            while (!st.empty()) {
                st.pop(); ++ans;
            }
            st.push(circles[i]);
        }
    }

    while (!st.empty())
    {
        st.pop();
        ++ans;
    }

    cout << ans + 1 << endl;

    return 0;
}