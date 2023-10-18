// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
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
using namespace atcoder;
using lli = long long;
// using mint = modint1000000007;
using mint = modint998244353;
// #define MOD 1000000007
#define MOD 998244353
#define INF (1LL << 60)
#define EPS (1e-10)
// typedef long long ll;
typedef pair<int, int> P;
typedef tuple<int, int, int> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (int i = 0; i < n; i++)
#define rep_r(i, k, n) for (int i = k; i > n; i--)
#define rep_s(i, k, n) for (int i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    int n, m;
    cin >> n >> m;
    int ll = 1;
    int lr = 1 + m;
    int rl = lr + 1;
    int rr = rl + m - 1;

    vector<P> ans;
    ans.emplace_back(P(ll, lr));
    if (rl < rr) ans.emplace_back(P(rl, rr));

    while (true) {
        ll++;
        lr--;
        if (ll >= lr) break;
        ans.emplace_back(P(ll, lr));
    }
    while (true) {
        rl++;
        rr--;
        if (rl >= rr) break;
        ans.emplace_back(P(rl, rr));
    }

    rep(i, m) cout << ans[i].first << ' ' << ans[i].second << "\n";

    return 0;
}