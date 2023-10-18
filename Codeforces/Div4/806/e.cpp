// #define _GLIBCXX_DEBUG
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
        vector<string> g(n);
        rep(i, n) cin >> g[i];

        ll ans = 0;
        rep(i, n) rep(j, n) {
            ll cnt = 0;
            if (g[i][j] == '1') cnt++;
            if (g[j][n - 1 - i] == '1') cnt++;
            if (g[n - 1 - i][n - 1 - j] == '1') cnt++;
            if (g[n - 1 - j][i] == '1') cnt++;
            ans += min(cnt, 4 - cnt);
            g[i][j] = '1';
            g[j][n - 1 - i] = '1';
            g[n - 1 - i][n - 1 - j] = '1';
            g[n - 1 - j][i] = '1';
        }
        cout << ans << "\n";
    }
    return 0;
}