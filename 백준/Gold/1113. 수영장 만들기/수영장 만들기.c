#include <stdio.h>
#include <stdlib.h>

#define MAX_HEIGHT 9 + 1
#define MAX_POOL_WIDTH 50 + 1
#define VEC_LEN 4

typedef struct _node
{
    int y;
    int x;
    struct _node *next;
} node;

typedef struct _queue
{
    node *head;
    node *tail;
    int count;
} queue;

typedef enum
{
    false,
    true
} bool;

int VEC[][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int n, m;
int pool[MAX_POOL_WIDTH][MAX_POOL_WIDTH];
bool visited[MAX_HEIGHT][MAX_POOL_WIDTH][MAX_POOL_WIDTH];
int edges[MAX_POOL_WIDTH * 4][2];
int water_filled;

void init_queue(queue *q)
{
    q->count = 0;
    q->head = NULL;
    q->tail = NULL;
}
void init_node(node *node, int y, int x)
{
    node->y = y;
    node->x = x;
    node->next = NULL;
}
void enque(queue *q, int y, int x)
{
    node *new_node = (node *)malloc(sizeof(node *));
    init_node(new_node, y, x);
    if (!q->count)
    {
        q->head = new_node;
    }
    else
    {
        q->tail->next = new_node;
    }
    q->tail = new_node;
    q->count++;
}
void deque(int *y, int *x, queue *q)
{
    if (!q->count)
    {
        return;
    }
    node *tmp = q->head;
    *y = q->head->y;
    *x = q->head->x;
    q->head = q->head->next;
    free(tmp);
    q->count--;
}

void bfs(queue *q, int level)
{
    while (q->count)
    {
        int y, x;
        deque(&y, &x, q);

        for (int i = 0; i < VEC_LEN; i++)
        {
            int ny, nx;
            ny = VEC[i][0] + y;
            nx = VEC[i][1] + x;

            if (0 < ny && ny < n - 1 && 0 < nx && nx < m - 1 && !visited[level][ny][nx]
                && ((pool[y][x] < pool[ny][nx] && level > pool[ny][nx])
                    || (pool[y][x] > pool[ny][nx] && pool[y][x] < level)
                    || (pool[y][x] == pool[ny][nx] && pool[y][x] < level)))
            {
                visited[level][ny][nx] = true;
                water_filled--;
                enque(q, ny, nx);
            }
        }
    }
}
int main()
{
    int edges_idx = 0;
    queue *q = (queue *)malloc(sizeof(queue *));
    init_queue(q);

    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++)
    {
        char line[MAX_POOL_WIDTH];
        scanf("%s", line);
        for (int j = 0; j < m; j++)
        {
            pool[i][j] = line[j] - '0';
            // Fill water
            if (0 < i && i < n - 1 && 0 < j && j < m - 1)
            {
                water_filled += (MAX_HEIGHT - 1) - pool[i][j];
            }
            else
            {
                edges[edges_idx][0] = i;
                edges[edges_idx][1] = j;
                edges_idx++;
            }
        }
    }

    for (int level = MAX_HEIGHT - 1; level > 1; level--)
    {
        for (int i = 0; i < edges_idx; i++)
        {
            enque(q, edges[i][0], edges[i][1]);
        }
        bfs(q, level);
    }

    printf("%d\n", water_filled);
    return 0;
}
