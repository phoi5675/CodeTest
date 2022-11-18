#include <iostream>
#include <algorithm>
using namespace std;

int N;
typedef struct _chem
{
    int lower;
    int upper;
    bool is_in_fridge;
} chem;
chem chems[100 + 10];

bool compare(chem first, chem second)
{
    return abs(first.upper - first.lower) < abs(second.upper - second.lower);
}

void InputData()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int lower, upper;
        cin >> lower >> upper;
        chems[i].lower = lower;
        chems[i].upper = upper;
        chems[i].is_in_fridge = false;
    }
}

int main()
{
    int ans = 0;

    InputData(); // 입력받는 부분

    // 여기서부터 작성

    sort(chems, chems + N, compare);
    // debug
    // for (int i = 0; i < N; i++)
    // {
    //     cout << chems[i].lower << '\t' << chems[i].upper << '\t' << abs(chems[i].upper - chems[i].lower) << '\n';
    // }

    for (int i = 0; i < N; i++)
    {
        // 이미 냉장고에 들어간 경우에는 pass
        if (chems[i].is_in_fridge)
        {
            continue;
        }
        chems[i].is_in_fridge = true;
        ans++;
        int lower_bound = chems[i].lower;
        int upper_bound = chems[i].upper;
        
        // 위에서 선택한 화학물질 보관 범위를 넘어서지 않는 한도에서 최소, 최대 온도 업데이트
        for (int j = i + 1; j < N; j++)
        {
            if (chems[j].is_in_fridge)
            {
                continue;
            }
            if (lower_bound <= chems[j].lower && chems[j].lower <= upper_bound)
            {
                lower_bound = chems[j].lower;
            }
            if (lower_bound <= chems[j].upper && chems[j].upper <= upper_bound)
            {
                upper_bound = chems[j].upper;
            }
        }

        // lower, upper 범위가 뒤집어진 경우
        if (upper_bound < lower_bound)
        {
            int tmp = lower_bound;
            lower_bound = upper_bound;
            upper_bound = lower_bound;
        }
        // debug
        // cout << lower_bound << '\t' << upper_bound << '\n';
        // lower_bound, upper_bound 사이에 있는 화학물질만 다시 검사
        for (int j = i + 1; j < N; j++)
        {
            if (!chems[j].is_in_fridge && (chems[j].lower <= lower_bound && upper_bound <= chems[j].upper))
            {
                chems[j].is_in_fridge = true;
            }
        }
    }

    cout << ans << endl; // 출력하는 부분
    return 0;
}
