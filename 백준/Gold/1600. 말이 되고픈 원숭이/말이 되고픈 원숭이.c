#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 200 + 1
#define MAX_HORSE_MOVES 30 + 1

typedef enum
{
    false,
    true
} bool;
typedef struct _node
{
    int y;
    int x;
    int moves;
    int horse_moves;
    struct _node *next;
} node;

typedef struct _queue
{
    node *front;
    node *rear;
    int count;
} queue;

int HORSE_VEC[][2] = {{-2, -1}, {-1, -2}, {1, -2}, {2, -1}, {2, 1}, {1, 2}, {-1, 2}, {-2, 1}};
int VEC[][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

int k, w, h;
int space[MAX_LEN][MAX_LEN];
bool visited[MAX_HORSE_MOVES][MAX_LEN][MAX_LEN];

node *init_node(int y, int x, int moves, int horse_moves)
{
    node *n = (node *)malloc(sizeof(node));
    n->y = y;
    n->x = x;
    n->moves = moves;
    n->horse_moves = horse_moves;

    return n;
}
void init_queue(queue *q)
{
    q->front = NULL;
    q->rear = NULL;
    q->count = 0;
}
void enque(queue *q, node *n)
{
    if (!q->count)
    {
        q->front = n;
        q->rear = q->front;
        q->front->next = NULL;
    }
    else
    {
        q->rear->next = n;
        q->rear = q->rear->next;
    }
    q->count++;
}

node deque(queue *q)
{
    node n;

    memcpy(&n, q->front, sizeof(node));

    node *tmp = q->front;
    q->front = q->front->next;
    q->count--;
    free(tmp);
    return n;
}

void traverse(queue *q, int vec[][2], int vec_len, node *n, int offset)
{
    for (int i = 0; i < vec_len; i++)
    {
        int ny, nx;
        ny = n->y + vec[i][0];
        nx = n->x + vec[i][1];
        if (0 <= ny && ny < h && 0 <= nx && nx < w && space[ny][nx] != 1 && !visited[n->horse_moves + offset][ny][nx])
        {
            visited[n->horse_moves + offset][ny][nx] = true;
            enque(q, init_node(ny, nx, n->moves + 1, n->horse_moves + offset));
        }
    }
}
int main()
{
    queue *q = (queue *)malloc(sizeof(queue));
    init_queue(q);
    node *n = init_node(0, 0, 0, 0);
    enque(q, n);

    scanf("%d", &k);
    scanf("%d %d", &w, &h);
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            scanf(" %d", &space[i][j]);
        }
    }

    while (q->count)
    {
        node front_node = deque(q);
        if (front_node.x == w - 1 && front_node.y == h - 1)
        {
            printf("%d\n", front_node.moves);
            exit(0);
        }
        if (front_node.horse_moves < k)
        {
            traverse(q, HORSE_VEC, 8, &front_node, 1);
        }
        traverse(q, VEC, 4, &front_node, 0);
    }

    printf("-1\n");
    return 0;
}
