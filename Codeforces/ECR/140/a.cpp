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
        vector<ll> x(3), y(3);
        rep(i, 3) cin >> x[i] >> y[i];

        sort(x.begin(), x.end());
        sort(y.begin(), y.end());

        bool ans = false;
        if (x[0] < x[1] and x[1] < x[2]) ans = true;
        if (y[0] < y[1] and y[1] < y[2]) ans = true;

        cout << (ans ? "Yes" : "No") << "\n";
    }
    return 0;
}