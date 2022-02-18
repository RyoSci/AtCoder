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
    if (s.length() < 26)
    {
        rep(i, 26)
        {
            bool ok = true;
            char t = 'a';
            rep(i, s.size())
            {
                if (s[i] == 'a' + i)
                {
                    /* code */
                    ok = false;
                    break;
                }
                t++;
            }
            if (ok)
            {
                /* code */
                cout << s + t << "\n";
            }
        }
    }
    else
    {
        vector<int> a;
        for (int i = s.size() - 1; i > -1; i--)
        {
            for (int j = 0; j < a.size(); j++)
            {
                if (s[i] < a[j])
                {
                    /* code */
                    cout << s.substr(0, i) + a.at(j) << "\n";
                    return;
                }
            }
            a.push_back(s[i]);
        }
    }
    cout << -1 << "\n";
    return 0;
}