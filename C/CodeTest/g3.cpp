#include <iostream>
#include <algorithm>
using namespace std;

int w, h, n;
int dir[100 + 10];
int len[100 + 10];
enum EDGE{ N = 1, S, W, E };
enum CASE{ SAME_AXIS = 1, PARA, CR_NW, CR_NE, CR_SW, CR_SE };
void InputData()
{
    cin >> w >> h;
    cin >> n;
    for (int i = 0; i <= n; i++)
    {
        cin >> dir[i] >> len[i];
    }
}
int get_case(int dg_axis, int shop_axis)
{
    if (dg_axis == shop_axis)
    {
        return SAME_AXIS;
    }
    else if ((dg_axis <= S && shop_axis <= S) || (dg_axis >= W && shop_axis >= W))
    {
        return PARA;
    }
    else if ((dg_axis == N && shop_axis == W) || (dg_axis == W && shop_axis == N))
    {
        return CR_NW;
    }
    else if ((dg_axis == N && shop_axis == E) || (dg_axis == E && shop_axis == N))
    {
        return CR_NE;
    }
    else if ((dg_axis == S && shop_axis == W) || (dg_axis == W && shop_axis == S))
    {
        return CR_SW;
    }
    else if ((dg_axis == S && shop_axis == E) || (dg_axis == E || shop_axis == S))
    {
        return CR_SE;
    }
    else
    {
        return -1;
    }
}
int get_len(int axis, bool is_other = false)
{
    if (axis == N || axis == S)
    {
        if (!is_other)
        {
            return w;
        }
        else
        {
            return h;
        }
    }
    else
    {
        if (!is_other)
        {
            return h;
        }
        else
        {
            return w;
        }
    }
}
int solve()
{
    int sum = 0, case_num = 0;
    int dg_axis = dir[n], dg_offset = len[n];
    int axis_len;
    for (int i = 0; i < n; i++)
    {
        case_num = get_case(dg_axis, dir[i]);
        // cout << case_num << '\t' << sum << endl;
        switch(case_num)
        {
            case SAME_AXIS:
                sum += abs(len[i] - dg_offset);
                break;
            case PARA:
                axis_len = get_len(dg_axis);
                sum += min(dg_offset + len[i], 
                            (axis_len - dg_offset) + (axis_len - len[i]))
                            + get_len(dg_axis, true);
                break;
            case CR_NW:
                sum += dg_offset + len[i];
                break;
            case CR_NE:
                if (dg_axis == N)
                {
                    sum += get_len(dg_axis) - dg_offset + len[i];
                }
                else
                {
                    sum += get_len(dir[i]) - len[i] + dg_offset;
                }
                break;
            case CR_SW:
                if (dg_axis == S)
                {
                    sum += get_len(dir[i]) - len[i] + dg_offset;
                }
                else
                {
                    sum += get_len(dg_axis) - dg_offset + len[i];
                }
                break;
            case CR_SE:
                sum += get_len(dg_axis) - dg_offset + get_len(dir[i]) - len[i];
                break;
            default:
                break;
        }
    }

    return sum;
}
int main()
{
    int ans = -1;

    InputData(); // 입력받는 부분

    // 여기서부터 작성
    ans = solve();
    cout << ans << endl; // 출력하는 부분
    return 0;
}