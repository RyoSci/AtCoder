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

int main() {
    double t;
    cin >> t;
    double l, x, y;
    cin >> l >> x >> y;
    ll q;
    cin >> q;
    double pi = acos(-1);
    rep(i, q) {
        double e;
        cin >> e;
        double alpha = 2 * e * pi / t;
        double yi, zi;
        yi = -l / 2 * sin(alpha);
        zi = l / 2 * (1 - cos(alpha));

        double sita;
        sita = atan2(zi, sqrt(x * x + (y - yi) * (y - yi)));
        //小数点以下の長さを指定
        cout << fixed << setprecision(15) << sita * 180 / pi << endl;
    }
    return 0;
}