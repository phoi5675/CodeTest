#include <iostream>
#include <stack>
using namespace std;
#define ISNUM(x) ((0 <= (x) - '0' && (x) - '0' <= 9))

const char CHILD='<';
const char END_CHILD='>';

typedef struct _node
{
    int childs;
    int depth;
    char name[15];
} node;

int N;
char A[20000 + 10];
void InputData()
{
    cin >> N >> A;
}

int extract_num(int &idx, char *name)
{
    int i = 0;
    while (ISNUM(A[idx]))
    {
        name[i++] = A[idx++];
    }
    return i;
}

int main()
{
    InputData(); // 입력받는 부분

    // 여기서부터 작성
    int i = 0;
    stack<node> tree;
    node head;
    head.depth = 0;
    head.childs = 0;
    int head_nptr = extract_num(i, head.name);

    tree.push(head);

    while (A[i])
    {
        node top = tree.top();
        // cout << i << '\t' << top.name << '\t' << top.depth << '\t' << top.childs << '\t' << A[i] << '\n';
        if (ISNUM(A[i]))
        {
            node n;
            int null_p = extract_num(i, n.name);
            n.name[null_p] = '\0';
            n.childs = 0;
            n.depth = top.childs >= 1 ? top.depth + 1 : top.depth;
            if (n.depth == N)
            {
                cout << n.name << ' ';
            }
            tree.push(n);
            continue;
        }
        else if (A[i] == CHILD)
        {
            top.childs++;
            tree.pop();
            tree.push(top);
        }
        else if (A[i] == END_CHILD)
        {
            if (top.childs == 2)
            {
                tree.pop();
            }
        }
        i++;
    }

    cout << '\n';
    return 0;
}