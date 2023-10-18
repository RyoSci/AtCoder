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
typedef long long ll;
typedef pair<ll, ll> P;
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll n, m;
    cin >> n >> m;
    string s;
    cin >> s;
    vector<ll> dp(n + 1, INF);
    dp[0] = 0;
    multiset<P> ms;

    vector<ll> from(n + 1, -1);

    rep_s(i, 1, n + 1) {
        ms.emplace(dp[i - 1], i - 1);
        if (i - 1 - m >= 0) {
            ms.erase(P(dp[i - 1 - m], i - 1 - m));
        }
        if (s[i] == '1') continue;
        auto [num, j] = *ms.begin();
        if (num == INF) continue;
        dp[i] = num + 1;
        from[i] = j;
    }

    if (dp[n] == INF)
        cout << -1 << "\n";
    else {
        ll now = n;
        vector<ll> ans;

        while (now != 0) {
            ans.emplace_back(now - from[now]);
            now = from[now];
        }
        reverse(ans.begin(), ans.end());
        for (auto a : ans) cout << a << " ";
        cout << endl;
    }
    return 0;
}