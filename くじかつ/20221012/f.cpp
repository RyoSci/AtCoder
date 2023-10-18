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

ll nCk(ll N, ll K) {
    ll ret = 1;
    if (K < 0 || N < K) return 0;
    for (ll i = 1; i <= K; ++i) {
        ret *= N--;
        ret /= i;
    }
    return ret;
}

int main() {
    ll n, a, b;
    cin >> n >> a >> b;
    vector<ll> v(n);
    for (ll i = 0; i < n; i++) cin >> v[i];
    sort(v.rbegin(), v.rend());

    ll cnt = 0;
    rep(i, a) cnt += v[i];

    P maxp = P(a, cnt);

    vector<ll> maxi;
    maxi.push_back(a);

    rep_s(i, a + 1, b + 1) {
        ll c = 0;
        rep(j, i) c += v[j];
        if (maxp.second * i == maxp.first * c) {
            maxi.emplace_back(i);
        } else if (maxp.second * i < maxp.first * c) {
            maxi.clear();
            maxi.emplace_back(i);
            maxp = P(i, c);
        }
    }

    map<ll, ll> d;
    rep(i, n) d[v[i]]++;

    ll ans = 0;
    rep_e(i, maxi) {
        map<ll, ll> tmp;
        rep(j, i) tmp[v[j]]++;
        ll cnt = 1;
        rep_e(e, tmp) {
            auto [key, val] = e;
            cnt *= nCk(d[key], val);
            // cout << d[key] << ' ' << val << ' ' << nCk(d[key], val) << " "
            //      << ans << "\n";
        }
        ans += cnt;
    }

    //小数点以下の長さを指定
    cout << fixed << setprecision(15) << double(maxp.second) / maxp.first
         << endl;
    cout << ans << "\n";
    return 0;
}