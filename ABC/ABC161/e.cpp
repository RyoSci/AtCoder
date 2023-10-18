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
    ll n, k, c;
    cin >> n >> k >> c;
    string s;
    cin >> s;

    vector<ll> ok(n, 1);
    vector<ll> work;
    set<ll> can;
    rep(i, n) {
        if (s[i] == 'o') {
            if (work.size() < k and (work.size() == 0 or work.back() + c < i)) {
                work.emplace_back(i);
            } else {
                can.insert(i);
            }
        }
    }

    rep_e(e, work) ok[e] = 0;

    ll pre = INF;
    can.insert(INF);
    ll m = work.size();
    rep_r(i, m - 1, -1) {
        ll r = pre - c - 1;
        ll l = work[i];
        auto posr = can.upper_bound(r);
        auto posl = can.upper_bound(l);
        if (posl != posr) {
            posr--;
            pre = *posr;
            can.erase(pre);
            can.insert(work[i]);
            ok[work[i]] = 1;
        } else {
            pre = work[i];
        }
    }

    rep(i, n) if (ok[i] == 0) cout << i + 1 << "\n";

    return 0;
}