#include <iostream>
#include <cmath>


using namespace std;

int main() {
    cout << fixed;
    cout.precision(3);
    int C, n;
    int arr[1000];
    cin >> C;

    while (C--)
    {
        cin >> n;
        int sum = 0, temp;
        double avg;

        for (size_t i = 0; i < n; i++)
        {
            cin >> temp;
            arr[i] = temp;
            sum += temp;
        }
        
        avg = (double)(sum / n);

        int cnt = 0;
        for (size_t i = 0; i < n; i++)
        {
            if (arr[i] > avg) ++cnt;
        }
        
        cout << ((double)cnt / n) * 100 << "%" << endl;
    }

    return 0;
}