#include <iostream>
#include <string>
#include <vector>

using namespace std;

string str;
int N, M;
vector<string> ord;

void input()
{
    str.resize(100000);
    cin >> str;
    N = str.size();
    cin >> M;
    string line;
    for (size_t i = 0; i < M; i++)
    {
        cin >> line;
        ord.push_back(line);
        if (line == "P") {
            cin >> line;
            ord[i] += " " + line;
        }
    }
}

void debug()
{
    cout << "=== debug ===" << endl;
    cout << str << endl;
    cout << N << ", " << M << endl;
    cout << "=== ord ===" << endl;
    for (size_t i = 0; i < ord.size(); i++)
    {
        cout << ord[i] << endl;
    }
    cout << "=== debug ===" << endl;
}

void solution()
{
    int cursor = N;
    for (auto elem : ord)
    {
        char a = elem[0];
        switch (a)
        {
        case 'P':
            str.insert(str.begin() + cursor, elem[2]);
            break;
        case 'L':
            if (cursor != 0)
                cursor--;
            break;
        case 'D':
            if (cursor != N)
                cursor++;
            break;
        case 'B':
            if (cursor != 0) {
                str.erase(str.begin() + --cursor);
            }
            break;
        default:
            break;
        }
        cout << str << " cursor: " << cursor << endl;
    }
}

int main()
{
    input();

    // debug();

    solution();

    // debug();

    cout << str << endl;

    return 0;
}