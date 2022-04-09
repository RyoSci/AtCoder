// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
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
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

double pi;
double a, b, c;

double f(double t) { return a * t + b * sin(c * t * pi); }

int main() {
    cin >> a >> b >> c;
    // double pi = acos(-1);
    pi = acos(-1);
    double l, r;
    if (a >= b * c * pi) {
        l = 0.0;
        r = 1000.0;
    } else {
        double ct0p, t0, t1;
        // 0~pi
        ct0p = acos(-a / (b * c * pi));
        t0 = ct0p / (c * pi);
        t1 = (2.0 * pi - ct0p) / (c * pi);
        l = 0.0;
        r = t0;
        rep(i, 1000) {
            r = t0 + 2.0 * i * pi / (c * pi);
            // 小数点以下の長さを指定
            // cout << fixed << setprecision(15) << "l " << l << " " << f(l)
            //      << endl;
            // cout << fixed << setprecision(15) << "r " << r << " " << f(r)
            //      << endl;
            if (f(r) >= 100.0) break;
            l = t1 + 2.0 * i * pi / (c * pi);
            // l = t;
        }
    }
    double m;
    while (l + EPS < r) {
        m = (l + r) / 2;
        if (f(m) >= 100.0)
            r = m;
        else
            l = m;
    }
    //小数点以下の長さを指定
    cout << fixed << setprecision(15) << l << endl;
    //小数点以下の長さを指定
    // cout << fixed << setprecision(15) << f(l) << endl;
    return 0;
}