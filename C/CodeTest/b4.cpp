#include <iostream>

using namespace std;

#define MAXN (10)
#define ROB ('2')
#define OBS ('1')
#define EMP ('0')
enum VEC
{
    D = 1,
    L,
    U,
    R
};

int vec[][5] = {{0, 0}, {1, 0}, {0, -1}, {-1, 0}, {0, 1}};

int N;
char map[MAXN + 10][MAXN + 10];
int dirseq[4];

int change_vec(int dir)
{
    return (dir + 1) % 4;
}
void InputData()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> map[i];
    }
    for (int i = 0; i < 4; i++)
    {
        cin >> dirseq[i];
    }
}
int main()
{
    int ans = 0;
    InputData(); //입력

    int dir = 0;
    int y = 0, x = 0;
    map[y][x] = ROB;
    bool moveable = true;
    while (moveable)
    {
        int v_idx = dirseq[dir];
        int dy = vec[v_idx][0], dx = vec[v_idx][1];
        int ny = y + dy, nx = x + dx;

        //debug
        // cout << "y : " << y << " x : " << x << " dir : " << v_idx << ' ' << ny << ' ' << nx << '\n'; 

        // 맵 안에서 이동하는 경우        
        if ((0 <= ny && ny < N) && (0 <= nx && nx < N))
        {
            if (map[ny][nx] == EMP)
            {
                map[ny][nx] = ROB;
                y = ny;
                x = nx;
                ans++;
            }
            else if (map[ny][nx] == OBS)
            {
                dir = change_vec(dir);
            }
            else if (map[ny][nx] == ROB)
            {
                moveable = false;
            }

        }
        // 맵 밖으로 이동하는 경우
        else
        {
            dir = change_vec(dir);
        }
    }

    // debug
    // for (int i = 0; i < N; i++)
    // {
    //     cout << map[i] << '\n';
    // }

    cout << ans << "\n"; //출력
    return 0;
}