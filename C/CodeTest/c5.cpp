#include <iostream>
#include <deque>

using namespace std;

#define MAXN ((int)5e5)
int N, K;
char str[MAXN + 10];
deque<char> st;
void InputData()
{
    cin >> N >> K;
    cin >> str;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    InputData(); //입력 받는 부분

    //여기서부터 작성
    int erased = 0;
    
    for (int i = 0; i < N; i++)
    {
        while (erased < K && !st.empty() && st.back() < str[i])
        {
            st.pop_back();
            erased++;
        }
        st.push_back(str[i]);
    }
    while (erased < K)
    {
        st.pop_back();
        erased++;
    }
    
    for (deque<char>::iterator itr = st.begin(); itr != st.end(); itr++)
    {
        cout << (*itr);
    }

    cout << '\n';

    return 0;
}