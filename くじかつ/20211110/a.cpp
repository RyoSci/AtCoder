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
    vector<bool> a(4);
    rep(i, 3)
    {
        string s;
        cin >> s;
        if (s[1] == 'B')
        {
            /* code */
            a[0] = 1;
        }
        else if (s[1] == 'R')
        {
            /* code */
            a[1] = 1;
        }
        else if (s[1] == 'G')
        {
            /* code */
            a[2] = 1;
        }
        else if (s[1] == 'H')
        {
            /* code */
            a[3] = 1;
        }
    }

    string s = "BRGH";
    rep(i, 4)
    {
        if (!a[i])
        {
            /* code */
            cout << 'A' << s[i] << 'C' << "\n";
        }
    }
    return 0;
}