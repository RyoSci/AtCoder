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
    ll n, k;
    cin >> n >> k;
    ll c = (n - 1) * (n - 2) / 2;
    if (k > c)
        cout << -1 << "\n";
    else {
        vector<P> ans;
        rep_s(i, 1, n) ans.emplace_back(make_pair(1, i + 1));
        rep_s(i, 1, n - 1) rep_s(j, i + 1, n) {
            if (c == k) {
                cout << ans.size() << "\n";
                rep_e(e, ans) { cout << e.first << ' ' << e.second << "\n"; }
                return 0;
            }
            ans.emplace_back(make_pair(i + 1, j + 1));
            c--;
        }
        cout << ans.size() << "\n";
        rep_e(e, ans) { cout << e.first << ' ' << e.second << "\n"; }
    }
    return 0;
}