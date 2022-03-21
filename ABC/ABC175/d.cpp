// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
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
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll n, k;
    cin >> n >> k;
    vector<ll> p(n);
    for (ll i = 0; i < n; i++) cin >> p[i];
    vector<ll> c(n);
    for (ll i = 0; i < n; i++) cin >> c[i];

    ll ans = -INF;
    // 全ての頂点を試す
    rep(i, n) {
        vector<ll> seen(n + 10, -1);
        // もう一度訪れるか、kが先に終わるまで続ける
        ll cnt = 0;
        ll to = i;
        // seen[to] = 0;
        ll cycle_num = -1;
        rep(j, k) {
            // cnt += c[to];
            // ans = max(ans, cnt);
            if (seen[to] != -1) {
                cycle_num = j - seen[to];
                break;
            }
            seen[to] = j;
            to = p[to];
            to--;
            cnt += c[to];
            ans = max(ans, cnt);
        }
        if (cycle_num == -1)
            continue;
        else {
            if (cnt > 0) {
                cnt = cnt * (k / cycle_num - 1);
                ans = max(ans, cnt);
                ll kk = k % cycle_num + cycle_num;
                rep(j, kk) {
                    to = p[to];
                    to--;
                    cnt += c[to];
                    ans = max(ans, cnt);
                }
            }
        }
    }
    cout << ans << "\n";
    return 0;
}