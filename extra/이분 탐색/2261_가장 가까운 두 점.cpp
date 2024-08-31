#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>

#define endl '\n'
#define pii pair<int, int>

using namespace std;

int n;
vector<pii> points;
set<pii> setted_points;

bool input () {
    cin >> n;
    points.reserve(n);
    
    for (size_t i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        points.push_back(make_pair(x, y));
        if (!setted_points.insert(make_pair(x, y)).second) {
            return false;
        }
    }
    return true;
}

void solution() {
    int dist = 0;
    
    // sort
    sort(points.begin(), points.end());

    // solution
    int mid = n / 2;

    // left
    int dist_left = INT32_MAX, dist_right = INT32_MAX;
    if (mid - 1 >= 0) {
        dist_left = (int)(pow(points[mid - 1].first, 2) + pow(points[mid - 1].second, 2));
    }
    if (mid + 1 < n) {
        dist_right = (int)(pow(points[mid + 1].first, 2) + pow(points[mid + 1].second, 2));
    }
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    if (!input()) {
        cout << 0 << endl;
        return 0;
    }

    solution();

    return 0;
}