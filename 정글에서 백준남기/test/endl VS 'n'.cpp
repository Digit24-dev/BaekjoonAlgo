#include <iostream>
#include <chrono>

using namespace std;
using namespace chrono;

int main() {
    const int iterations = 10000;

    // 측정: cout << endl;
    auto start1 = high_resolution_clock::now();
    for (int i = 0; i < iterations; ++i) {
        cout << "Hello" << endl;
    }
    auto end1 = high_resolution_clock::now();

    // 측정: cout << '\n';
    auto start2 = high_resolution_clock::now();
    for (int i = 0; i < iterations; ++i) {
        cout << "Hello" << '\n';
    }
    auto end2 = high_resolution_clock::now();

    // 결과 출력
    cout << "Time for endl: " 
         << duration_cast<milliseconds>(end1 - start1).count() << " ms\n";
    cout << "Time for '\\n': " 
         << duration_cast<milliseconds>(end2 - start2).count() << " ms\n";

    return 0;
}
