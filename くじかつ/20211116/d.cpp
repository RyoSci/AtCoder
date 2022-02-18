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
    int l, q;
    cin >> l >> q;
    vector<int> c(q);
    vector<int> x(q);
    rep(i, q)
    {
        cin >> c[i] >> x[i];
    }
    set<int> s;
    s.insert(0);
    s.insert(l);
    rep(i, q)
    {
        if (c[i] == 1)
        {
            /* code */
            s.insert(x[i]);
        }
        else
        {
            /* code */

            auto iter = s.lower_bound(x[i]);
            // int index = distance(s.begin(), iter);
            // cout << index << "\n";
            int res = 0;
            int left, right;
            right = *iter;
            iter--;
            left = *iter;

            cout
                << right - left << "\n";
        }
    }

    return 0;
}