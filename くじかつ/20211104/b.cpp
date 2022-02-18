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
    rep(i, pow(2, 3))
    {
        int tmp = s[0] - '0';
        string res = "";
        res += s[0];
        rep(j, 3)
        {
            if ((i >> j) & 1)
            {
                /* code */
                tmp += (s[j + 1] - '0');
                res += '+';
                res += s[j + 1];
            }
            else
            {
                tmp -= (s[j + 1] - '0');
                res += '-';
                res += s[j + 1];
            }
        }
        if (tmp == 7)
        {
            cout << res << "=7"
                 << "\n";
            return 0;
        }
    }

    return 0;
}