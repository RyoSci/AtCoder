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
    string n;
    cin >> n;
    vector<ll> mod(3, 0);
    ll tot = 0;
    rep_e(c, n) {
        mod[(c - '0') % 3]++;
        tot += c - '0';
        tot %= 3;
    }
    ll ans = INF;
    if (tot == 0)
        ans = 0;
    else if (tot == 1) {
        if (mod[1] > 0)
            ans = 1;
        else if (mod[2] > 1)
            ans = 2;
    } else {
        if (mod[2] > 0)
            ans = 1;
        else if (mod[1] > 1)
            ans = 2;
    }
    if (ans >= n.size())
        cout << -1 << "\n";
    else
        cout << ans << "\n";

    return 0;
}