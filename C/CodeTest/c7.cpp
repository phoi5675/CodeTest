#include <iostream>
#include <algorithm>
#include <vector>
 
using namespace std;
 
int N;              //히스토그램수
int H[100000 + 10]; //히스토그램 높이
vector<int> stk;
bool InputData()
{
    cin >> N;
    if (N == 0)
        return false;
 
    for (int i = 0; i < N; i++)
    {
        cin >> H[i];
    }
    return true;
}
 
long long solve()
{
    long long area = 0;
    for (int i = 0; i < N; i++)
    {
        while (!stk.empty() && H[stk.back()] > H[i])
        {
            long long height = H[stk.back()];
            long long len = i;
            stk.pop_back();
             
            if (!stk.empty())
            {
                len = i - stk.back() - 1;
            }
            area = max(area, len * height);
        }
        // 스택에는 항상 오름차순으로 저장됨
        stk.push_back(i);
    }
 
    while (!stk.empty())
    {
        long long height = H[stk.back()];
        long long len = N;
        stk.pop_back();
        if (!stk.empty())
        {
            len = N - stk.back() - 1;
        }
        area = max(area, len * height);
    }
    return area;
}
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
 
    long long ans = -1;
    while (InputData())
    { //입력받는 부분
 
        //여기서부터 작성
        ans = solve();
        cout << ans << "\n"; //출력하는 부분
    }
    return 0;
}