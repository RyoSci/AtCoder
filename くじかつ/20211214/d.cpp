#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
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
#define rep_e(c, s) for (auto c : s)

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];
    map<int, int> s, t;
    s[0] = 0, t[0] = 0;
    rep(i, n) {
        if (i % 2 == 0)
            s[v[i]]++;
        else
            t[v[i]]++;
    }
    vector<pair<int, int>> s_e, t_e;
    rep_e(item, s) {
        int key = item.first;
        int val = item.second;
        s_e.push_back({val, key});
    }
    rep_e(item, t) {
        int key = item.first;
        int val = item.second;
        t_e.push_back({val, key});
    }
    sort(s_e.begin(), s_e.end());
    reverse(s_e.begin(), s_e.end());
    sort(t_e.begin(), t_e.end());
    reverse(t_e.begin(), t_e.end());
    int ans = 0;
    if (s_e[0].second != t_e[0].second) {
        ans += n / 2 - s_e[0].first;
        ans += n / 2 - t_e[0].first;
    } else {
        ans += n / 2 - s_e[0].first;
        ans += n / 2 - max(s_e[1].first, t_e[1].first);
    }
    cout << ans << "\n";
    return 0;
}