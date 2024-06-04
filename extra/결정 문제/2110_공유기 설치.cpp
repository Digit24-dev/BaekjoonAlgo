#include <iostream>
#include <vector>
#include <algorithm>

/*
핵심 
기준이 인덱스가 아닌 간격을 기준 잡아서 이분 탐색을 진행할 것.

-> 최대 간격을 반으로 접어가며 계산한다.
*/

#define MAX_N 200000

using namespace std;

int N, C;
vector<int> pos_house;

void input()
{
    cin >> N >> C;
    pos_house.resize(N);
    for (size_t i = 0; i < N; i++)
    {
        cin >> pos_house[i];
    }
    sort(pos_house.begin(), pos_house.end());
}

int solution()
{
    int start = 1;
    int end = pos_house[N - 1] - pos_house[0];
    int st, router, ans = 0;

    while (start <= end)
    {
        int mid = (start + end) / 2;
        router = 1;
        st = pos_house[0];
        
        for (size_t i = 1; i < N; i++)
        {
            if (pos_house[i] - st >= mid)
            {
                router++;
                st = pos_house[i];
            }
        }

        if (router >= C)
        {
            ans = max(ans, mid);
            start = mid + 1;
        }
        else
            end = mid - 1;
    }
    return ans;
}

int main() {

    input();

    cout << solution();

    return 0;
}