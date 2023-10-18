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
    ll h, w, a, b;
    cin >> h >> w >> a >> b;

    auto dfs = [&](auto dfs, ll id, ll mask, ll acnt) -> ll {
        if (id == h * w) {
            if (mask == (1 << (h * w)) - 1 and acnt == a) {
                return 1;
            } else
                return 0;
        }

        ll x = id / w;
        ll y = id % w;

        ll ans = 0;

        if (acnt < a) {
            // 横に貼る
            if (y < w - 1 and !((mask >> id) & 1) and
                !((mask >> (id + 1)) & 1)) {
                ll nmask = mask;
                nmask |= (1 << id);
                nmask |= (1 << (id + 1));
                ans += dfs(dfs, id + 1, nmask, acnt + 1);
            }
            // 縦に貼る
            if (x < h - 1 and !((mask >> id) & 1) and
                !((mask >> (id + w)) & 1)) {
                ll nmask = mask;
                nmask |= (1 << id);
                nmask |= (1 << (id + w));
                ans += dfs(dfs, id + 1, nmask, acnt + 1);
            }
        }
        // Bを使える場合
        if (!(mask >> id & 1)) {
            ll nmask = mask;
            nmask |= (1 << id);
            ans += dfs(dfs, id + 1, nmask, acnt);
        } else {
            ans += dfs(dfs, id + 1, mask, acnt);
        }

        return ans;
    };

    ll ans = dfs(dfs, 0, 0, 0);

    cout << ans << "\n";

    return 0;
}