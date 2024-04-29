#include <iostream>
#include <vector>
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
    vector<pair<int, int>> drawn;

    cin >> n;

    while (n--)
    {
        cin >> x >> r;
        circles.push_back(make_pair(x, r));
    }
    
    sort(circles.begin(), circles.end(), [](pair<int, int> a, pair<int, int> b) {
        if (a.second == b.second) return a.first < b.first;
        return a.second < b.second;
    });

    // 반지름 기준 정렬된 원 부터 그린다.
    for (size_t i = 0; i < circles.size(); i++)
    {
        // 자기 자신의 영역 그림.
        ans += 1;
        
        // 이미 그려진 영역에서 겹치는 영역 있을 시에 + 1
        for (auto elem : drawn)
        {
            // 원 외부
            if (check_outside(circles[i], elem)) continue;
            // 원 내부
            if (check_inside(circles[i], elem)) {
                // 경계선
                if (check_boarder(circles[i], elem))
                    continue;
                // 겹치는 경우
                ans += 1;
            }
        }
        drawn.push_back(circles[i]);
    }

    // 원 겹치는 경우 그리기
    for (auto elem : drawn)
    {
        
    }

    cout << ans + 1 << endl;

    return 0;
}