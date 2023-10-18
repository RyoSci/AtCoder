// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
#include <atcoder/modint>
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
using mint = modint1000000007;
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
    ll n, m;
    cin >> n >> m;
    vector<vector<ll>> a(2 * n, vector<ll>(m, 0));
    rep(i, 2 * n) rep(j, m) {
        char c;
        cin >> c;
        if (c == 'G') a[i][j] = 0;
        if (c == 'C') a[i][j] = 1;
        if (c == 'P') a[i][j] = 2;
        ;
    }

    vector<P> ans;
    rep(i, 2 * n) { ans.push_back(make_pair(0, i)); }

    rep(i, m) {
        sort(ans.begin(), ans.end());

        vector<P> tmp;
        rep(j, n) {
            auto [li, lj] = ans[j * 2];
            auto [ri, rj] = ans[j * 2 + 1];
            li = -li;
            ri = -ri;
            if ((a[lj][i] + 3 - 1) % 3 == a[rj][i]) ri++;
            if ((a[lj][i] + 3 + 1) % 3 == a[rj][i]) li++;
            tmp.push_back(make_pair(-li, lj));
            tmp.push_back(make_pair(-ri, rj));
        }
        ans = tmp;
    }
    sort(ans.begin(), ans.end());
    rep(i, 2 * n) {
        auto [l, r] = ans[i];
        cout << r + 1 << "\n";
    }

    return 0;
}