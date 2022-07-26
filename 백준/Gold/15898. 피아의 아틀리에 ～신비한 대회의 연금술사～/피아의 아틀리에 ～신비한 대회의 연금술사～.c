#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BOARD_SIZE 5
#define ING_SIZE 4
#define PERM_SIZE 3
#define ROTATIONS 4
#define ARR_SIZE 10

int res = 0;
typedef enum
{
    false,
    true
} bool;
typedef enum
{
    CHAR,
    INT
} types;

char color_pot[5][6];
int effect_pot[5][5] = {0};

char colors[ARR_SIZE][4][5];
int effects[ARR_SIZE][4][4];

int offset[4][2] = {{0, 0}, {1, 0}, {0, 1}, {1, 1}};

void dfs_mix_ingredients(int *perms, char (*color_pot)[6], int (*effect_pot)[5], int level)
{
    if (level == 3)
    {
        int r = 0, g = 0, b = 0, y = 0;
        for (int i = 0; i < BOARD_SIZE; i++)
        {
            for (int j = 0; j < BOARD_SIZE; j++)
            {
                switch (color_pot[i][j])
                {
                case 'R':
                    r += effect_pot[i][j];
                    break;
                case 'G':
                    g += effect_pot[i][j];
                    break;
                case 'B':
                    b += effect_pot[i][j];
                    break;
                case 'Y':
                    y += effect_pot[i][j];
                    break;
                }
            }
        }
        int calc = 7 * r + 5 * b + 3 * g + 2 * y;
        if (res < calc)
        {
            res = calc;
        }
        return;
    }

    for (int ofs = 0; ofs < 4; ofs++)
    {
        int off_y = offset[ofs][0], off_x = offset[ofs][1];
        for (int rot = 0; rot < 4; rot++)
        {
            int y = 0, x = 0;
            char(*_color_pot)[BOARD_SIZE + 1] = malloc(sizeof(char[BOARD_SIZE][BOARD_SIZE + 1]));
            int(*_effect_pot)[BOARD_SIZE] = malloc(sizeof(int[BOARD_SIZE][BOARD_SIZE]));

            memcpy(_color_pot, color_pot, sizeof(char) * BOARD_SIZE * (BOARD_SIZE + 1));
            memcpy(_effect_pot, effect_pot, sizeof(int) * BOARD_SIZE * BOARD_SIZE);
            for (int i = 0; i < ING_SIZE; i++)
            {
                for (int j = 0; j < ING_SIZE; j++)
                {
                    switch (rot)
                    {
                    case 0:
                        y = i;
                        x = j;
                        break;
                    case 1:
                        y = 3 - j;
                        x = i;
                        break;
                    case 2:
                        y = 3 - i;
                        x = 3 - j;
                        break;
                    case 3:
                        y = j;
                        x = 3 - i;
                        break;
                    }
                    char color = colors[perms[level]][y][x];
                    int effect = effects[perms[level]][y][x] + _effect_pot[i + off_y][j + off_x];
                    if (color != 'W')
                    {
                        _color_pot[off_y + i][off_x + j] = color;
                    }
                    if (effect < 0)
                    {
                        effect = 0;
                    }
                    else if (effect > 9)
                    {
                        effect = 9;
                    }
                    _effect_pot[off_y + i][off_x + j] = effect;
                }
            }
            dfs_mix_ingredients(perms, _color_pot, _effect_pot, level + 1);
        }
    }
}

void dfs_permutation(int *perms, int n, bool *visited, int idx)
{
    if (idx == PERM_SIZE)
    {
        dfs_mix_ingredients(perms, color_pot, effect_pot, 0);
        return;
    }

    for (int i = 0; i < n; i++)
    {
        if (!visited[i])
        {
            visited[i] = true;
            perms[idx] = i;
            dfs_permutation(perms, n, visited, idx + 1);
            visited[i] = false;
        }
    }
}
int main(int argc, char const *argv[])
{
    int n;

    scanf("%d", &n);

    int perms[3] = {0};
    bool visited[10] = {false};
    // Initialize color pot
    for (int i = 0; i < BOARD_SIZE; i++)
    {
        for (int j = 0; j < BOARD_SIZE; j++)
        {
            color_pot[i][j] = 'W';
        }
        color_pot[i][BOARD_SIZE] = '\0';
    }

    // Get inputs
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                scanf("%d", &effects[i][j][k]);
            }
        }
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                scanf(" %c", &colors[i][j][k]);
            }
            colors[i][j][4] = '\0';
        }
    }

    dfs_permutation(perms, n, visited, 0);

    printf("%d\n", res);
    return 0;
}
