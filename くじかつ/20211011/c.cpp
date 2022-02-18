#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <stack>
using namespace std;
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (int i = 0; i < n; i++)

int main()
{
    string s;
    cin >> s;
    int k;
    cin >> k;

    bool flag = true;
    int index;
    char c;
    for (int i = 0; i < s.length(); i++)
    {
        if (s.at(i) != '1')
        {
            flag = false;
            index = i;
            c = s[i];
            break;
        }
    }
    if (flag)
    {
        /* code */
        cout << 1 << "\n";
    }
    else
    {
        if (k <= index)
        {
            /* code */
            cout << 1 << "\n";
        }
        else
        {
            cout << c << "\n";
        }
    }

    return 0;
}