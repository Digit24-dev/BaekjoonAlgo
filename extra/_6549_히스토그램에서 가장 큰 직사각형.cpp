#include <iostream>
#include <vector>

#define MAX 100001

using namespace std;
vector<int> squares;
int n;

inline bool isRanged(int h) {
    return 0 <= h && h < n;
}

int main() {
    squares.reserve(MAX);

    cin >> n;

    while (n)
    {
        /* logic -> n ^ 2 */
        int max_ssize = 0;
        for (size_t i = 0; i < n; i++)
            cin >> squares[i];
        
        for (size_t i = 0; i < n - 1; i++)
        {
            int ssize = squares[i], cur_h = squares[i];
            for (size_t j = i + 1; j < n; j++)
            {
                cur_h = min(cur_h, squares[j]);
                ssize = cur_h * (j - i + 1);
                max_ssize = max(max_ssize, ssize);
            }
        }
        /* logic */
        cout << max_ssize << endl;
        cin >> n;
    }

    return 0;
}