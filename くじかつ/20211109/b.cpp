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
    map<string, int> d;
    rep(i, n)
    {
        string s;
        cin >> s;
        d[s]++;
    }
    int max_cnt = 0;
    vector<pair<int, string>> p;
    for (auto item : d)
    {
        string key = item.first;
        int val = item.second;
        max_cnt = min(max_cnt, -val);
        p.push_back(make_pair(-val, key));
    }
    sort(p.begin(), p.end());
    for (auto x : p)
    {
        if (x.first == max_cnt)
        {
            /* code */
            cout << x.second << "\n";
        }
    }
    return 0;
}