#include <iostream>
#include <memory.h>
#include <algorithm>

using namespace std;

#define MAX_N 16

int N;
int answer = 0;

// index: i / val: j
int visited[MAX_N];
int map[MAX_N][MAX_N];

inline bool check(int lev) {
	for(int i=0; i < lev; i++) 
		if (visited[i] == visited[lev] || abs(visited[i] - visited[lev]) == lev - i) return false;
	
	return true;
}

void dfs(int depth)
{
	// 종료 조건
	if (depth == N) {
		answer++;
		return;
	}
	
	for (int i = 0; i < N; i++)
	{
		visited[depth] = i;
		if (check(depth)) {
			dfs(depth + 1);
		}
	}
}

int main() {
	cin >> N;

	dfs(0);
	
	cout << answer << endl;

	return 0;
}