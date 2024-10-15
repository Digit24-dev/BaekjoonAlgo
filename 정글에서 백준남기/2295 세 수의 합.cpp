#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

// 최대 O(N^2 log N)

using namespace std;

int N;
int arr[1001];
set<int> sumSet;
set<int> origin;

int main()
{
    cin >> N;
    int ans = 0;
    
    for (size_t i = 0; i < N; i++){
        cin >> arr[i];
        origin.insert(arr[i]);
    }
    
    // 두 수의 합
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            sumSet.insert(arr[i] + arr[j]);
    
    for (int k = N - 1; k >= 0; k--)
    {
        for (int i = 0; i < N; i++)
        {
            if (sumSet.find(arr[k] - arr[i]) != sumSet.end())
                ans = max(ans, arr[k]);
        }
    }
    
    cout << ans << endl;

    return 0;
}