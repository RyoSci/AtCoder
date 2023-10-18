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
// #define MOD 1000000007
#define MOD 998244353
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
        ll m, s;
        cin >> m >> s;
        vector<ll> b(m);
        for (ll i = 0; i < m; i++) cin >> b[i];
        sort(b.begin(), b.end());
        ll mx = b.back();

        set<ll> c;
        rep(i, m) c.insert(b[i]);

        if (c.size() != m) {
            cout << "NO"
                 << "\n";
            return 0;
        }

        rep_s(i, 1, mx) {
            if (c.count(i) == 0) s -= i;
        }

        mx++;
        while (s > 0) {
            s -= mx;
            mx++;
        }

        if (s == 0)
            cout << "YES"
                 << "\n";
        else
            cout << "NO"
                 << "\n";
    }
    return 0;
}