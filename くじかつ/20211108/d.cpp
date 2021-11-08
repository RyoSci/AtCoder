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
#define rep_r(i, k, n) for (int i = k; i > n; i--)
#define rep_s(i, k, n) for (int i = k; i < n; i++)

int main()
{
    string s;
    cin >> s;
    string t;
    cin >> t;
    int n, m;
    n = s.length();
    m = t.length();

    rep_r(i, n - m, -1)
    {
        bool flag = true;
        rep(j, m)
        {
            if (s[i + j] == t[j] or s[i + j] == '?')
            {
                /* code */
                continue;
            }
            else
            {
                flag = false;
                break;
            }
        }
        if (flag)
        {
            /* code */
            rep(j, n)
            {
                if (j < i | i + m - 1 < j)
                {
                    /* code */
                    if (s[j] == '?')
                    {
                        cout << 'a';
                    }
                    else
                    {
                        cout << s[j];
                    }
                }
                else if (i <= j && j <= i + m - 1)
                {
                    /* code */
                    cout << t[j - i];
                }
            }
            return 0;
        }
    }
    cout << "UNRESTORABLE"
         << "\n";
    return 0;
}