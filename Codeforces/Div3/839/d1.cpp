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
        ll n;
        cin >> n;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        ll min_x = 1e9;
        ll max_x = 0;
        rep(i, n - 1) {
            if (a[i] < a[i + 1]) {
                min_x = min(min_x, (a[i] + a[i + 1]) / 2);
            } else if (a[i] > a[i + 1]) {
                max_x = max(max_x, (a[i] + a[i + 1] + 1) / 2);
            }
        }
        if (max_x <= min_x)
            cout << max_x << "\n";
        else
            cout << -1 << "\n";
    }
    return 0;
}