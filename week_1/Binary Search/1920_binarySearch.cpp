#include <iostream>
#include <algorithm>

using namespace std;

#define MAX 100001
#define endl '\n'

int arr1[MAX];

int N, M;

int bin_search_recursive(int _first, int _second, int key)
{
	int mid = (_first + _second) / 2;
	if (_first > _second)
		return 0;
	else {
		if (arr1[mid] == key)
			return 1;
		else
		{
			if (arr1[mid] > key)
				bin_search_recursive(mid + 1, _second, key);
			else if (arr1[mid] < key)
				bin_search_recursive(_first, mid - 1, key);
		}
	}
}

void bin_search(int _first, int _second, int key)
{
	int mid;
	while (_first <= _second)
	{
		mid = (_first + _second) / 2;
		
		if (arr1[mid] == key) {
			cout << 1 << endl;
			return;		// <======== 종료 조건 추가 안함......!!!!
		}
		else if (arr1[mid] < key)
			_first = mid + 1;
		else
			_second = mid - 1;
	}
	cout << 0 << endl;
	return;
}

void solution()
{
	int key;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> arr1[i];
	}
	
	sort(arr1, arr1 + N);

	cin >> M;
	for (int i = 0; i < M; i++)
	{
		cin >> key;
		bin_search(0, N - 1, key);
	}
}


int main()
{
	ios::sync_with_stdio(0);
	cin.tie(NULL);

	solution();

	return 0;
}