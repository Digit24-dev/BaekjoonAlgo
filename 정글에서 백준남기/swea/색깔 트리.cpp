#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

/*
    명령들
    (1) 노드 추가
    - 고유 번호 mid, 부모 노드 번호 pid, 색깔 color, 최대 깊이 max depth
    - color 1 ~ 5 // 빨 주 노 초 파
    - pid - 1) 이 노드는 새로운 트리의 루트 노드
    - max depth는 해당 노드를 루트로 하는 서브트리의 최대 깊이 (자기자신 1)
    - $$ 만약 max depth로 인해서 모순이 발생시 현재 노드는 추가하지 않는다.
    
    (2) 색 변경
    - 서브 트리의 모든 노드 색 변경

    (3) 색 조회
    - 특정 노드 mid 색 조회

    (4) 점수 조회
    - 모든 노드의 가치 계산, 제곱의 합을 출력
    - 가치 : 해당 노드를 루트로하는 서브트리 내 서로 다른 색깔의 수로 정의

    (1) 100 mid pid color max_depth         20000
    (2) 200 mid color                       50000
    (3) 300 mid                             20000
    (4) 400                                 100
*/

struct node
{
    int m_id;
    int p_id;
    int color;
    int max_depth;
    vector<node*> subnodes;
};
vector<node*> roots;
node* nodePointer[100001];
node tree[20000];
int idx = 0;

bool nodeCheck(int m_id, int cnt)
{
    bool ret = false;
    if (nodePointer[m_id]->max_depth <= cnt)
        return true;
    if (nodePointer[m_id]->p_id != -1)
        ret = nodeCheck(nodePointer[m_id]->p_id, cnt + 1);
    return ret;
}

void addNode(int mid, int pid, int color, int mdepth)
{
    // 부모 노드의 max_depth가 1이하일 경우
    if (pid != -1 && nodeCheck(pid, 1))
        return;
    
    // 동적 배열로 등록
    tree[idx].m_id = mid;
    tree[idx].p_id = pid;
    tree[idx].color = color;
    tree[idx].max_depth = mdepth;

    // 노드 포인터에 등록
    nodePointer[mid] = &tree[idx];

    // 루트 노드
    if (pid == -1) {
        roots.push_back(&tree[idx]);
    }
    else {
        // 부모 노드에 자식 정보 등록
        nodePointer[pid]->subnodes.push_back(nodePointer[mid]);
    }
    ++idx;
}

void changeColor(int mid, int color)
{
    nodePointer[mid]->color = color;
    
    for (size_t i = 0; i < nodePointer[mid]->subnodes.size(); i++)
    {
        changeColor(nodePointer[mid]->subnodes[i]->m_id, color);
    }
}

int queryColor(int mid)
{
    return nodePointer[mid]->color;
}

int score(bool bucket[6], int m_id)
{
    node *me = nodePointer[m_id];
    
    int inner = 0, ret = 0;
    bool i_bucket[6] = { 0, };

    for (size_t i = 0; i < me->subnodes.size(); i++)
    {
        memset(i_bucket, false, sizeof(i_bucket));
        ret += score(i_bucket, me->subnodes[i]->m_id);
        for (size_t i = 1; i < 6; i++)
            bucket[i] |= i_bucket[i];
    }

    bucket[me->color] = true;
    for (size_t i = 1; i < 6; i++) {
        inner += bucket[i] | i_bucket[i];
        //bucket[i] |= i_bucket[i];
    }

    return ret + (inner * inner);
}

int queryScore()
{
    int total = 0;

    for (auto& e : roots)
    {
        bool bucket[6] = { 0, };
        int sum = 0;

        total += score(bucket, e->m_id);
    }

    return total;
}

int main() {
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);

    int Q, Ord; // 1 ~ 100,000
    int mid, pid, color, mdepth;

    //FILE* fp;
    //freopen_s(&fp, "input (4).txt", "r", stdin);

    cin >> Q;
    
    while (Q--)
    {
        cin >> Ord;
        switch (Ord)
        {
        case 100:
            cin >> mid >> pid >> color >> mdepth;
            addNode(mid, pid, color, mdepth);
            break;
        case 200:
            cin >> mid >> color;
            changeColor(mid, color);
            break;
        case 300:
            cin >> mid;
            cout << queryColor(mid) << endl;
            break;
        case 400:
            cout << queryScore() << endl;
            break;
        }
    }

    return 0;
}