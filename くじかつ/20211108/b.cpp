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
    int n;
    cin >> n;
    set<char> t;
    rep(i, n)
    {
        char s;
        cin >> s;
        t.insert(s);
    }
    if (t.size() == 3)
    {
        /* code */
        cout << "Three"
             << "\n";
    }
    else if (t.size() == 4)
    {
        /* code */
        cout << "Four"
             << "\n";
    }

    return 0;
}