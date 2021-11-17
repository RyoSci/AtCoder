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
#include <iomanip>
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
    string res = "";
    bool flag = false;
    for (char c : s)
    {
        if (c == '.')
        {
            /* code */
            flag = true;
            continue;
        }
        if (flag)
        {
            /* code */
            if (c - '0' >= 5)
            {
                int tmp = stoi(res);
                tmp++;
                /* code */
                cout << tmp << "\n";
                return 0;
            }
            else
            {
                /* code */
                cout << res << "\n";
                return 0;
            }
        }
        else
        {
            /* code */
            res += c;
        }
    }

    return 0;
}