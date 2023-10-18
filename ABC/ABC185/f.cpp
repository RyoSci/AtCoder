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
    ll n, q;
    cin >> n >> q;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<fenwick_tree<ll>> bits(30, fenwick_tree<ll>(n + 1));

    auto cal = [&](ll x, ll i) {
        for (ll digit = 0; digit < 30; digit++) {
            bits[digit].add(i, x % 2);
            x >>= 1;
            if (x == 0) {
                break;
            }
        }
    };

    for (ll i = 0; i < n; i++) {
        cal(a[i], i + 1);
    }

    vector<long long> twos(40);
    twos[0] = 1;
    for (ll i = 1; i < 40; i++) {
        twos[i] = twos[i - 1] * 2;
    }

    vector<long long> ans;
    for (ll i = 0; i < q; i++) {
        ll t, x, y;
        cin >> t >> x >> y;
        if (t == 1) {
            cal(y, x);
        } else {
            long long res = 0;
            for (ll digit = 0; digit < 30; digit++) {
                res += bits[digit].sum(x, y + 1) % 2 * twos[digit];
            }
            ans.push_back(res);
        }
    }

    for (long long a : ans) {
        cout << a << "\n";
    }

    return 0;
}