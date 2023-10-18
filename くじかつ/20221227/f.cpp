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
using mint = modint1000000007;
// using mint = modint998244353;
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
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> p, m;

    rep(i, n) {
        if (a[i] >= 0)
            p.emplace_back(a[i]);
        else
            m.emplace_back(a[i]);
    }

    sort(p.begin(), p.end());
    sort(m.begin(), m.end());

    mint ans = mint(1);
    priority_queue<ll> pq;

    if (k <= min(m.size(), k) / 2 * 2 + p.size()) {
        if (k % 2 == 1) {
            ans *= p.back();
            p.pop_back();
        }
        reverse(p.begin(), p.end());
        for (ll i = 0; 2 <= p.size() and i + 1 < p.size(); i += 2) {
            pq.emplace(p[i] * p[i + 1]);
        }
        for (ll i = 0; 2 <= m.size() and i + 1 < m.size(); i += 2) {
            pq.emplace(m[i] * m[i + 1]);
        }

        rep(i, k / 2) {
            ans *= pq.top();
            pq.pop();
        }
    } else {
        ans *= -1;
        rep(i, n) pq.emplace(-abs(a[i]));
        rep(i, k) {
            ans *= -pq.top();
            pq.pop();
        }
    }
    cout << ans.val() << "\n";
    return 0;
}