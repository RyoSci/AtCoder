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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n;
        cin >> n;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        vector<P> ai_i;
        vector<ll> b;

        rep(i, n) {
            if (a[i] < i + 1) {
                ai_i.push_back({a[i], i + 1});
                b.push_back(a[i]);
            }
        }
        sort(ai_i.begin(), ai_i.end());
        sort(b.begin(), b.end());
        ll ans = 0;
        rep_e(e, ai_i) {
            auto [ai, i] = e;
            ll dis = b.end() - upper_bound(b.begin(), b.end(), i);
            ans += dis;
        }
        cout << ans << "\n";
    }
    return 0;
}