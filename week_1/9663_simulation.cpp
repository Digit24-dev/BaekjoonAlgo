#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

#define MAX_N 16

// 12시 부터 시계 방향
int di[8] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dj[8] = { 0, 1, 1, 1, 0, -1,-1, -1 };

int N;
int answer = 0;

bool isRanged(int ni, int nj) {
	return ni >= 0 && ni < N && nj >= 0 && nj < N;
}

int map[MAX_N][MAX_N];
// 1: queen, -1:  can't go

void block(int i, int j) {

	for (int dir = 0; dir < 8; dir++)
	{
		int ni = i, nj = j;

		do{
			ni += di[dir];
			nj += dj[dir];
			
			if (isRanged(ni, nj))
				map[ni][nj] += -1;
			else
				break;

		} while (true);
	}
}

void unblock(int i, int j) {

	for (int dir = 0; dir < 8; dir++)
	{
		int ni = i, nj = j;

		do{
			ni += di[dir];
			nj += dj[dir];
			if (isRanged(ni, nj))
				map[ni][nj] += 1;
			else
				break;
		} while (true);
	}
}

void dfs(int depth, int ci, int cj)
{
	// 종료 조건
	if (depth == N) {
		answer++;
		return;
	}
	// 처리
	// 여기서 dfs를 적용하여 depth 가 N 까지 진행할 수 있도록 할 것.
	
	for (int i = ci + 1; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (map[i][j] == 0) {
				// 재귀
				map[i][j] = 1;
				block(i, j);

				dfs(depth + 1, i, j);

				map[i][j] = 0;
				unblock(i, j);
			}
		}
	}
}

int main() {
	cin >> N;

	// 초기
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			map[i][j] = 1;
			block(i, j);

			dfs(1, i, j);

			map[i][j] = 0;
			unblock(i, j);
		}
	}

	cout << answer << endl;

	return 0;
}