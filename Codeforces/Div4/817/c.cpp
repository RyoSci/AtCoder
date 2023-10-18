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
        vector<string> a(n), b(n), c(n);
        rep(i, n) { cin >> a[i]; }
        rep(i, n) { cin >> b[i]; }
        rep(i, n) { cin >> c[i]; }

        map<string, ll> da, db, dc;
        rep(i, n) {
            da[a[i]]++;
            db[b[i]]++;
            dc[c[i]]++;
        }

        ll aa = 0, bb = 0, cc = 0;
        rep(i, n) {
            ll cnt = 0;
            cnt += da[a[i]];
            cnt += db[a[i]];
            cnt += dc[a[i]];
            if (cnt == 1)
                aa += 3;
            else if (cnt == 2)
                aa += 1;
        }

        rep(i, n) {
            ll cnt = 0;
            cnt += da[b[i]];
            cnt += db[b[i]];
            cnt += dc[b[i]];
            if (cnt == 1)
                bb += 3;
            else if (cnt == 2)
                bb += 1;
        }
        cout << "\n";
        rep(i, n) {
            ll cnt = 0;
            cnt += da[c[i]];
            cnt += db[c[i]];
            cnt += dc[c[i]];
            if (cnt == 1)
                cc += 3;
            else if (cnt == 2)
                cc += 1;
        }
        cout << aa << ' ' << bb << ' ' << cc << "\n";
    }
    return 0;
}