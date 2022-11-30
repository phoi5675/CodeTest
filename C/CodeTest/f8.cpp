#include <iostream>
using namespace std;
int W;      //사용할 금액
int A[6];   //각 동전 개수(갖고 있는)
int sol[6]; //답

int coin[] = {500, 100, 50, 10, 5, 1};
int Solve()
{
    int sum = 0; //사용하는 동전 총 개수
    // 1.갖고 있는 돈 계산
    int total = 0;
    for (int i = 0; i < 6; i++)
    {
        total += A[i] * coin[i];
    }
    total -= W; //남길 금액
    // 2.남기는 금액을 최소 동전 으로...(최대 동전 사용)
    for (int i = 0; i < 6; i++)
    {
        int cnt = total / coin[i]; // i번 동전 남길 개수(계산)
        if (cnt > A[i])
        { //계산한 결과가 갖고 있는 동전보다 많은 경우
            cnt = A[i];
        }
        sol[i] = A[i] - cnt; //사용 동전 수 = 갖고 있는 동전 수 - 남길 동전 수
        sum += sol[i];
        total -= coin[i] * cnt;
    }
    return sum;
}

void InputData()
{
    cin >> W;
    for (int i = 0; i < 6; i++)
    {
        cin >> A[i];
    }
}
void OutputData(int ans)
{
    cout << ans << "\n";
    for (int i = 0; i < 6; i++)
    {
        cout << sol[i] << " ";
    }
    cout << "\n";
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int ans = -1;

    InputData(); //입력받는 부분

    ans = Solve(); //여기서부터 작성

    OutputData(ans); //출력하는 부분
    return 0;
}