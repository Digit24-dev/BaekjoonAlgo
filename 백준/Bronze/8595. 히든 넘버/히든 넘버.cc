#include <iostream>
#include <string>

using namespace std;

int main() 
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int N;
    long long sum = 0;
    string str, temp;

    cin >> N;
    cin >> str;
    
    for (size_t i = 0; i < N; i++)
    {
        if (isdigit(str[i])) 
        {
            temp += str[i];
        }
        else 
        {
            if (!temp.empty())
            {
                sum += stoll(temp);
                temp = "";
            }
        }
    }

    if (temp != "") sum += stoll(temp);
    
    cout << sum << endl;

    return 0;
}