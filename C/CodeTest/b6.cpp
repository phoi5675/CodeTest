#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define MAXN ((int)1e4)

int N;
vector<pair<int, int> > students;
int present;
int absent;
void InputData(void)
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int arr, left;
        cin >> arr >> left;
        students.push_back(make_pair(arr, left));
    }
}

bool compare(pair<int, int> first, pair<int, int> second)
{
    return first.first < second.first;
}

int main(void)
{
    InputData(); // 입력받는 부분

    // 여기서부터 작성
    sort(students.begin(), students.end(), compare);
    // 초기값 설정
    int cur_present = students[0].second - students[0].first, cur_absent = students[0].first;
    present = cur_present;
    absent = cur_absent;

    // for (int i = 0; i < N; i++)
    // {
    //     cout << students[i].first << ' ' << students[i].second << '\n';
    // }

    // 이전 학생이 떠난 시각과 현재 학생이 도착한 시간 비교
    int prev_left = students[0].second;
    for (int i = 1; i < N; i++)
    {
        int cur_arrv = students[i].first, cur_left = students[i].second;
        // cout << cur_arrv << '\t' << cur_left << '\n';
        // 이전 학생이 떠나기 전에 현재 학생이 들어온 경우, 계속 학생이 머무른 상태
        if (cur_arrv <= prev_left)
        {
            if (cur_left <= prev_left)
            {
                continue;
            }
            cur_present += (cur_left - prev_left);
            prev_left = cur_left;
        }
        else
        {
            // 앞의 학생이 떠나는 시간과 뒤의 학생이 도착하는 시간 사이에 빈 공간이 생기는 경우,
            // prev값 갱신
            absent = max(absent, cur_arrv - prev_left);
            cur_present = (cur_left - cur_arrv);
            prev_left = cur_left;
        }
        present = max(present, cur_present);
    }
    

    cout << present << " " << absent << endl; // 출력하는 부분
    return 0;
}