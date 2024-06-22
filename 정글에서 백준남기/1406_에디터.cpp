#include <iostream>
#include <list>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string str;
    int n;
    cin >> str;
    cin >> n;

    list<char> editor(str.begin(), str.end());
    auto cursor = editor.end(); // 초기 커서를 문자열 끝으로 설정

    while (n--) {
        char command;
        cin >> command;

        if (command == 'L') {
            if (cursor != editor.begin()) {
                --cursor;
            }
        } else if (command == 'D') {
            if (cursor != editor.end()) {
                ++cursor;
            }
        } else if (command == 'B') {
            if (cursor != editor.begin()) {
                cursor = editor.erase(--cursor);
            }
        } else if (command == 'P') {
            char ch;
            cin >> ch;
            editor.insert(cursor, ch);
        }
    }

    for (char ch : editor) {
        cout << ch;
    }

    return 0;
}
