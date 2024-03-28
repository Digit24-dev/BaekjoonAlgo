#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> arr;
vector<int> ans;

void dfs(int depth, int idx)
{
    // 종료 조건
    if (depth == 7)
    {
        int sum = 0;
        for (auto& i : ans)
        {
            sum += i;
        }
        if (sum == 100)
        {
            sort(ans.begin(), ans.end());
            for (auto& i : ans)
            {
                cout << i << endl;
            }
            exit(0);
        }
        else
            return;
    }

    for (int i = depth; i < arr.size(); i++)
    {
        ans.push_back(arr[i]);
        dfs(depth + 1, i + 1);
        ans.pop_back();
    }
}


int main()
{
    // input
    for (size_t i = 0; i < 9; i++)
    {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }

    dfs(0, 0);

    return 0;
}