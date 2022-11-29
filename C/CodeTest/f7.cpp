#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;
#define MAXB (9)
#define MAXN ((int)1e5)
int B, N; // 배의 수, 승객의 수
int S[MAXB+10]; // 최대수용무게
int P[MAXN+10]; // 승객 무게 배열
int p_sum[MAXN + 10];
int used[MAXB + 10];
int ans = -1;
void InputData(){
    cin >> B >> N;
    for (int i=0; i<B; i++){
        cin >> S[i];
    }
    for (int i=0; i<N; i++){
        cin >> P[i];
    }
}
void fill_p_sum()
{
    p_sum[0] = P[0];
    for (int i = 1; i < N; i++)
    {
        p_sum[i] = p_sum[i - 1] + P[i];
    }
}
int bin_search(int left, int right, int pivot)
{
    int mid;
    int res = left;
    while (left <= right)
    {
        mid = (left + right) / 2;
        if (p_sum[mid] <= pivot)
        {
            left = mid + 1;
            res = mid;
        }
        else
        {
            right = mid - 1;
        }
    }
    return res;
}
bool dfs(int psger_idx, int ship_used, int cur_capa)
{
    // printf("psgr_idx : %d, psgr : %d, ship_used : %d, cur_capa : %d\n", 
    //     psger_idx, p_sum[psger_idx], ship_used, cur_capa);
    if (psger_idx == N - 1)
    {
        int capa_left = 0;
        for (int i = 0; i < B; i++)
        {
            if (!used[i])
            {
                capa_left += S[i];
            }
        }
        // printf("cur_capa : %d, capa : %d\n", cur_capa, capa_left);
        ans = max(ans, capa_left);
        return true;
    }

    for (int ship = 0; ship < B; ship++)
    {
        if (used[ship])
        {
            continue;
        }
        used[ship] = true;
        ship_used++;
        cur_capa += S[ship];
        int load_max_idx = bin_search(psger_idx, N - 1, cur_capa);

        // printf("%d %d / %d %d\n", load_max_idx, ship, p_sum[load_max_idx], cur_capa);
        dfs(load_max_idx, ship_used, p_sum[load_max_idx]);
        // for (int i = psger_idx; i < N; i++)
        // {
        //     if ((i < N - 1 && p_sum[i - 1] <= cur_capa && cur_capa < p_sum[i])
        //         || (i == N - 1 && p_sum[i] <= cur_capa))
        //     {
        //         break;
        //     }
        // }
        used[ship] = false;
        ship_used--;
        cur_capa -= S[ship];
    }
    return false;
}
int main(void){

    InputData();//입력받는 부분

    //여기서부터 작성
    fill_p_sum();
    dfs(0, 0, 0);
    
    cout << ans << endl;//출력하는 부분
    return 0;
}
