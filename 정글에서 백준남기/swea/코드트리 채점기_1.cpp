#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <unordered_map>
#include <set>

using namespace std;

/*
* (1) 채점기 준비
* N개의 채점기, u: url 도메인/문제ID
* 도메인: 알파벳 소문자 + '.' 으로 이루어짐, ID 1 ~ 1000 000 000
* 0초) 우선순위가 1 u[0]인 초기 문제에 대한 요청이 들어옴.
* 채점 task는 채점 대기 큐에 들어감
* 
* (2) 채점 요청
* t초에 p url, 요청이 들어옴
* task는 대기큐에 들어감
* url이 하나라도 있으면 큐에 추가하지 않음.
* 
* (3) 채점 시도
* 남은 task중 우선순위가 가장 높은 채점 task
* <채점 불가 항목>
* - 도메인이 현재 채점을 진행 중일 경우
* - 가장 최근에 진행된 채점 시간이 start, 종료시간이 start + gap, 현재 시간 t < start + 3*gap 일 경우
* <측채가>
* - p의 번호가 작을 수록 우선순위 높다
* - 우선 순위 동일 시에 큐 순서대로
* t초에 채점 가능한 task가 하나라도 있으면 쉬고 있는 채점기 중 가장 번호가 작은 채점기가 가장 높은 채점 task에 대한 채점을 시작
* 없으면 무시
* 
* (4) 채점 종료
* t 초에 Jid 번 채점기가 진행하던 채점이 종료 -> 쉬는 상태
* 진행하던 채점이 없으면 무시
* 
* (5) 채점 대기 큐 조회
* 시간 t에 채점 대기 큐에 있는 채점 task의 수를 출력
* 
* [명령]
* (1) 100 N u0
* (2) 200 t p u 
* (3) 300 t -> t초에 채점 대기 큐에서 즉시 채점이 가능한 경우 우선순위가 가장 높은 채점 task를 골라 채점을 진행
* (4) 400 t jid -> 
* (5) 500 t
* 
*/

int Q, N; // 1 ~ 50000
int Ord;
//1 ≤ 도메인의 길이 ≤ 19
//1 ≤ 주어지는 서로 다른 도메인의 수 ≤ 300
//1 ≤ 문제 ID ≤ 1, 000, 000, 000
//1 ≤ p ≤ N
//1 ≤ Jid ≤ N
//1 ≤ t ≤ 1, 000, 000

struct task
{
    int priority;
    long id;
    string uri = "";
    string dom;
    int start_time;
    int duration;

    struct Comparator{
        bool operator()(const task& a, const task& b) const {
            return a.priority > b.priority;
        }
    };
};

struct state
{
    bool running;
    task job;
};

state worker[50001];

priority_queue<task, vector<task>, task::Comparator> wait_q;
unordered_map<string, task> history;
set<string> wait_q_set;

void init(string line)
{
    task temp;
    temp.uri = line;
    temp.start_time = 0;
    temp.priority = 1;
    
    auto ptr = line.find('/');
    temp.dom = line.substr(0, ptr);

    wait_q_set.insert(line);
    wait_q.push(temp);
}

void request(int t, int p, string line)
{
    task temp;
    temp.priority = p;
    temp.start_time = t;
    temp.uri = line;

    auto ptr = line.find('/');
    temp.dom = line.substr(0, ptr);

    if (wait_q_set.insert(line).second)
        wait_q.push(temp);
}

void tryCheck(int t)
{
    if (wait_q.empty())
        return;

    task cur = wait_q.top();
    
    // 현재 채점 중인 도메인
    for (size_t i = 1; i <= N; i++)
    {
        if (worker[i].running && cur.dom == worker[i].job.dom)
            return;
    }

    // 조건2
    auto iter = history.find(cur.dom);
    if (iter != history.end() && t < history[cur.dom].start_time + history[cur.dom].duration * 3)
        return;

    // 가동
    for (size_t i = 1; i <= N; i++)
    {
        if (!worker[i].running) {
            worker[i].running = true;
            worker[i].job.dom = cur.dom;
            worker[i].job.duration = cur.duration;
            worker[i].job.priority = cur.priority;
            worker[i].job.start_time = t;
            worker[i].job.uri = cur.uri;

            wait_q.pop();
            auto iter = wait_q_set.find(cur.uri);
            wait_q_set.erase(iter);

            break;
        }
    }
}

void offJob(int t, int id)
{
    state *_t = &worker[id];
    
    if (!_t->running)
        return;

    _t->running = false;
    _t->job.duration = t - _t->job.start_time;

    task temp;
    history.insert(make_pair(worker[id].job.dom, temp));
    task* _d = &history[_t->job.dom];

    _d->dom = _t->job.dom;
    _d->duration = _t->job.duration;
    _d->start_time = _t->job.start_time;
    _d->uri = _t->job.uri;

    /*temp.dom = worker[id].job.dom;
    temp.duration = worker[id].job.duration;
    temp.id = worker[id].job.id;
    temp.priority = worker[id].job.priority;
    temp.start_time = worker[id].job.start_time;*/

    history.insert(make_pair(temp.dom, temp));
}

size_t peekQ(int t)
{
    return wait_q.size();
}

int main() {
    
    int Ord, t, p, id;

    FILE* fp;
    freopen_s(&fp, "input (6).txt", "r", stdin);

    cin >> Q;
    while (Q--)
    {
        string line;
        cin >> Ord;
        switch (Ord)
        {
        case 100:
            cin >> N >> line;
            init(line);
            break;
        case 200:
            cin >> t >> p >> line;
            request(t, p, line);
            break;
        case 300:
            cin >> t;
            tryCheck(t);
            break;
        case 400:
            cin >> t >> id;
            offJob(t, id);
            break;
        case 500:
            cin >> t;
            cout << peekQ(t) << endl;
            break;
        }
    }

    return 0;
}