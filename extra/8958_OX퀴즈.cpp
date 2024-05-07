#include <iostream>

using namespace std;

int main() {
    cin.tie(0); cout.tie(0);
    ios_base::sync_with_stdio(0);
    string line;
    int n, ans, cnt;
    cin >> n;

    while (n--)
    {
        ans = 0; cnt = 1;
        cin >> line;

        for (size_t i = 0; i < line.size(); i++)
        {
            if (line[i] == 'O')
                ans += cnt++;
            else {
                cnt = 1;
            }
        }
        cout << ans << endl;
    }

    return 0;
}