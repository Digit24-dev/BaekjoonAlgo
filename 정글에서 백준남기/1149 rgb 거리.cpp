#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <memory.h>

using namespace std;

#define cord pair<int, int>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);

#define MAX 1000 + 1

int N; 
int house[MAX][3];
int ans = 0;

int main()
{
    FASTIO

    int rgb[3];

    cin >> N;
    for (size_t i = 0; i < N; i++)
    {
        cin >> rgb[0] >> rgb[1] >> rgb[2];
        house[i][0] = min(house[i-1][1], house[i-1][2]) + rgb[0];
        house[i][1] = min(house[i-1][0], house[i-1][2]) + rgb[1];
        house[i][2] = min(house[i-1][0], house[i-1][1]) + rgb[2];
    }
    
    ans = house[N-1][0] > house[N-1][1] ? 
            house[N-1][1] > house[N-1][2] ? house[N-1][2] : house[N-1][1] 
            : 
            house[N-1][0] > house[N-1][2] ? house[N-1][2] : house[N-1][0];

    cout << ans << endl;

    return 0;
}

// 이렇게도 풀 수 있다.
// 타뷸레이션으로 생각하는 것이 조금 더 편하고 빠르게 만들 수 있지만, 조금만 더 생각해보면 굳이 테이블을 만들 필요가 없다는 걸 알 수 있다.

// #include <cstdio>
// #include <algorithm>
// using namespace std;

// int main() {
// 	int n, r, g, b, c[3] = { 0, }; scanf("%d", &n);
// 	while (n--) {
// 		scanf("%d %d %d", &r, &g, &b);
// 		r += min(c[1], c[2]);
// 		g += min(c[0], c[2]);
// 		b += min(c[0], c[1]);
// 		c[0] = r, c[1] = g, c[2] = b;
// 	}
// 	printf("%d", min(r, min(g, b)));
// }
