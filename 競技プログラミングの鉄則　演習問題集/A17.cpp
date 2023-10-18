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
    ll n;
    cin >> n;
    vector<ll> a(n + 1);
    for (ll i = 2; i < n + 1; i++) cin >> a[i];
    vector<ll> b(n + 1);
    for (ll i = 3; i < n + 1; i++) cin >> b[i];

    vector<ll> dp(n + 1, INF);
    dp[1] = 0;
    vector<ll> pre(n + 1, -1);

    rep_s(i, 1, n) {
        if (i + 1 <= n) {
            if (dp[i + 1] > dp[i] + a[i + 1]) {
                dp[i + 1] = dp[i] + a[i + 1];
                pre[i + 1] = i;
            }
        }
        if (i + 2 <= n) {
            if (dp[i + 2] > dp[i] + b[i + 2]) {
                dp[i + 2] = dp[i] + b[i + 2];
                pre[i + 2] = i;
            }
        }
    }

    ll now = n;
    vector<ll> ans;
    while (now != -1) {
        ans.emplace_back(now);
        now = pre[now];
    }

    reverse(ans.begin(), ans.end());
    cout << ans.size() << "\n";
    for (auto a : ans) cout << a << " ";
    cout << endl;

    return 0;
}