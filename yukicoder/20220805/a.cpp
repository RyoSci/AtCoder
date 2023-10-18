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
    ll n, s;
    cin >> n >> s;

    ll num;
    rep_s(i, 1, n + 2) {
        if (i * (i + 1) / 2 > s) {
            num = i - 1;
            break;
        }
    }
    ll rm;
    ll start = num * (num + 1) / 2;
    rep(i, num + 1) {
        ll now = start + i;
        if (now == s) {
            rm = num + 1 - i;
            break;
        }
    }

    vector<ll> ans;
    rep(i, num + 1) {
        if (i + 1 != rm) ans.emplace_back(i + 1);
    }
    cout << ans.size() << "\n";
    for (auto a : ans) cout << a << " ";
    cout << endl;
    return 0;
}