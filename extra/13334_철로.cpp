#include <iostream>
#include <queue>

#define endl  '\n'

using namespace std;

int n, d, ans = 0;
vector<pair<int, int>> temp;
priority_queue<int, vector<int>, less<>> pq;

void input()
{
  cin >> n;
  temp.reserve(n);
  for (size_t i = 0; i < n; i++)
  {
    int a, b;
    cin >> a >> b;
    if (a < b)
      temp.push_back(make_pair(a, b));
    else
      temp.push_back(make_pair(b, a));
  }
  cin >> d;
}

void solution()
{
  sort(temp.begin(), temp.end(), [](pair<int, int> a, pair<int, int> b) {
    if (a.second == b.second) return a.first < b.first;
    return a.second < b.second;
  });

  for (int i = 0; i < temp.size(); i++)
  {
    int start = temp[i].first;
    int end   = temp[i].second;

    if (end - start > d) continue;

    pq.push(start);

    while (!pq.empty())
    {
      if (pq.top() < end - d) pq.pop();
      else {
        ans = max(ans, (int)pq.size());
        break;
      }
    }
  }
  
}

int main() {
  cin.tie(0);

  input();

  solution();

  cout << ans << endl;

  return 0;
}