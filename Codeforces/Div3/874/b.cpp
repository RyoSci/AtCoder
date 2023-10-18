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
        ll n, k;
        cin >> n >> k;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        vector<ll> b(n);
        for (ll i = 0; i < n; i++) cin >> b[i];

        vector<P> ab;
        rep(i, n) { ab.emplace_back(a[i], i); }
        sort(ab.begin(), ab.end());
        sort(b.begin(), b.end());

        vector<ll> bb(n);
        rep(i, n) { bb[ab[i].second] = b[i]; }

        for (auto a : bb) cout << a << " ";
        cout << endl;
    }
    return 0;
}