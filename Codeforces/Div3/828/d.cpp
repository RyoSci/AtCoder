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
using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n;
        cin >> n;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        ll cnt = 0;
        rep(i, n) {
            while (a[i] % 2 == 0) {
                cnt++;
                a[i] /= 2;
            }
        }

        priority_queue<ll> pq;
        rep_s(i, 1, n + 1) {
            ll j = i;
            ll tmp = 0;
            while (j % 2 == 0) {
                tmp++;
                j /= 2;
            }
            if (tmp > 0) pq.push(tmp);
        }

        ll ans = 0;
        while (pq.size() > 0) {
            if (n <= cnt) break;
            cnt += pq.top();
            pq.pop();
            ans++;
        }
        if (n <= cnt)
            cout << ans << "\n";
        else
            cout << -1 << "\n";
    }
    return 0;
}