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
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    set<int> s;
    rep(i, n)
    {
        int tmp = a[i];
        for (int j = 2; j * j <= a[i]; j++)
        {
            while (true)
            {
                /* code */
                if (tmp % j == 0)
                {
                    /* code */
                    tmp /= j;
                    s.insert(j);
                }
                else
                {
                    /* code */
                    break;
                }
            }
        }

        if (tmp != 1)
        {
            /* code */
            s.insert(tmp);
        }
    }

    vector<int> table(m + 1, 1);
    for (auto i : s)
    {
        if (i == 1)
        {
            continue;
        }
        for (int j = i; j <= m; j += i)
        {
            table[j] = 0;
        }
    }
    int res = 0;
    vector<int> ans;

    rep_s(i, 1, m + 1)
    {
        if (table[i] == 1)
        {
            /* code */
            res++;
            ans.push_back(i);
        }
    }
    cout << res << "\n";
    sort(ans.begin(), ans.end());
    for (auto i : ans)
    {
        cout << i << "\n";
    }
    return 0;
}