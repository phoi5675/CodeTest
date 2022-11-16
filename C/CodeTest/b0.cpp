#include <iostream>
#include <map>
#include <algorithm>
#include <list>
#include <string>

using namespace std;

int N;
char S[10000 + 10][20 + 10];
map<string, list<int> > dict;
list<string> ordered_list;
void InputData()
{
    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        cin >> S[i];
    }
}

bool isUnique()
{
    map<string, list<int> >::iterator itr;
    for (itr = dict.begin(); itr != dict.end(); itr++)
    {
        if ((*itr).second.size() > 1)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    InputData(); // 입력받는 부분

    // 여기서부터 작성
    for (int i = 1; i <= N; i++)
    {
        if (dict.find(S[i]) == dict.end())
        {   
            string s = string(S[i]);
            list<int> l(1, i);
            dict.insert(make_pair(s, l));
            ordered_list.push_back(s);
        }
        else
        {
            dict[S[i]].push_back(i);
        }
    }

    if (isUnique())
    {
        cout << "unique" << endl;
    }
    else
    {
        list<string>::iterator itr;
        for (itr = ordered_list.begin(); itr != ordered_list.end(); itr++)
        {
            string key = (*itr);
            if (dict[key].size() <= 1)
            {
                continue;
            }
            cout << key << ' ';
            list<int>::iterator int_itr;
            for (int_itr = dict[key].begin(); int_itr != dict[key].end(); int_itr++)
            {
                cout << (*int_itr) << ' ';
            }
            cout << endl;
        }
    }
    return 0;
}