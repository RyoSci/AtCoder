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
    Int n, k;
    cin >> n >> k;
    vector<pair<Int, Int>> ab;
    for (int i = 0; i < n; i++)
    {
        Int a, b;
        cin >> a >> b;
        ab.push_back({a, b});
    }
    sort(ab.begin(), ab.end());
    rep(i, n)
    {
        if (k >= ab[i].first)
        {
            /* code */
            k += ab[i].second;
        }
    }
    cout << k << "\n";
    return 0;
}