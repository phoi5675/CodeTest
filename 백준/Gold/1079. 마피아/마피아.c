#include <stdio.h>
#include <string.h>

#define max(a, b) (a) > (b) ? (a) : (b)
#define KILLED -100000
int res, n, unjin;
int r[17][17];

int find_max(int *ary, int len)
{
    int idx = len - 1;
    for (int i = len - 1; i >= 0; i--)
    {
        if (ary[i] >= ary[idx])
        {
            idx = i;
        }
    }
    return idx;
}
void dfs(int civil_left, int *guilty_level, float elapsed)
{
    if ((!civil_left && guilty_level[unjin] != KILLED) || guilty_level[unjin] == KILLED)
    {
        res = max(res, (int)elapsed);
        return;
    }

    if ((civil_left + 1) % 2 == 0)
    {
        for (int i = 0; i < n; i++)
        {
            if (guilty_level[i] == KILLED || i == unjin)
            {
                continue;
            }
            int guilty_copied[17];
            memcpy(guilty_copied, guilty_level, sizeof(int) * n);
            for (int j = 0; j < n; j++)
            {
                if (guilty_copied[j] == KILLED)
                {
                    continue;
                }
                guilty_copied[j] += r[i][j];
            }
            guilty_copied[i] = KILLED;
            dfs(civil_left - 1, guilty_copied, elapsed + 0.5);
        }
    }
    else
    {
        int guilty_copied[17];
        memcpy(guilty_copied, guilty_level, sizeof(int) * n);
        int chosen = find_max(guilty_copied, n);
        guilty_copied[chosen] = KILLED;
        dfs(civil_left - 1, guilty_copied, elapsed + 0.5);
    }
}
int main()
{
    int guilty_level[17] = {0};

    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf(" %d", &guilty_level[i]);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf(" %d", &r[i][j]);
        }
    }

    scanf("%d", &unjin);
    int civil_left = n - 1;
    dfs(civil_left, guilty_level, (n % 2 == 0) ? 0.5 : 0);

    printf("%d\n", res);

    return 0;
}
