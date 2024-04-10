#include <iostream>
#include <string>
#include <vector>
#include <memory.h>
using namespace std;

#define endl '\n'

int main(){
	cin.tie(0); cout.tie(0);
	ios_base::sync_with_stdio(0);
	
    int M;
    string op;
//    vector<bool> S(20, false);
	bool S[20] = {false, };
    cin >> M;

    while(M--){
        cin >> op;
        
        if (op == "empty") {
            // S = vector<bool>(20, false);
            memset(S, false, sizeof(S));
            continue;
        }else if (op == "all") {
            // S = vector<bool>(20, true);
            memset(S, true, sizeof(S));
            continue;
        }
        int num;
        cin >> num;
        if (op == "add") {
            S[num - 1] = true;
        }else if (op == "remove"){
            S[num - 1] = false;
        }else if (op == "check") {
            cout << S[num - 1] << endl;
        }else if (op == "toggle") {
            S[num - 1] = !S[num - 1];
        }
    }
}