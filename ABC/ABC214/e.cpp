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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n;
        cin >> n;
        vector<T> lr;
        map<ll, vector<ll>> d;
        vector<ll> tot;

        rep(i, n) {
            ll l, r;
            cin >> l >> r;
            d[l].emplace_back(r);
            tot.emplace_back(l);
        }

        tot.emplace_back(INF);
        sort(tot.begin(), tot.end());

        ll now = tot[0];
        priority_queue<ll> pq;
        bool ans = true;
        while (now <= 1000000000) {
            rep_e(r, d[now]) { pq.emplace(-r); }

            if (pq.size()) {
                if (-pq.top() < now) {
                    ans = false;
                    break;
                } else {
                    pq.pop();
                    now++;
                }

            } else {
                auto iter = lower_bound(tot.begin(), tot.end(), now);
                now = *iter;
            }
        }
        if (pq.size()) ans = false;
        cout << (ans ? "Yes" : "No") << "\n";
    }

    return 0;
}