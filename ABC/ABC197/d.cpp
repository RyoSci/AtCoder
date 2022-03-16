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

int main() {
    ll n;
    cin >> n;
    double x0, y0, xn2, yn2;
    cin >> x0 >> y0 >> xn2 >> yn2;

    // 半径を求める
    double r = sqrt(powl(x0 - xn2, 2.0) + powl(y0 - yn2, 2.0)) / 2.0;

    // 中心を原点に移動
    double cx, cy;
    cx = (x0 + xn2) / 2.0;
    cy = (y0 + yn2) / 2.0;

    x0 -= cx;
    y0 -= cy;
    xn2 -= cx;
    yn2 -= cy;

    // 0点を(r,0)に回転する 移動角をalphaとする
    double pi = acos(-1);
    double alpha = atan2(y0, x0);
    // double alpha = atan(y0 / x0); # - x
    // -でπ/2までしか値域がないので別途処理が必要

    // cout << fixed << setprecision(15) << x0 << " " << y0 << endl;
    x0 = r;
    y0 = 0.0;

    // 1点の角度を求める sita
    double sita = 360.0 / n / 180.0 * pi;

    // cout << alpha * 180 / pi << "\n";
    // cout << sita * 180 / pi << "\n";
    double x1, y1;
    x1 = r * cos(sita + alpha);
    y1 = r * sin(sita + alpha);

    // cout << fixed << setprecision(15) << x1 << " " << y1 << endl;
    // cout << fixed << setprecision(15) << xn2 << " " << yn2 << endl;
    // 元の場所に平行移動
    x1 += cx;
    y1 += cy;

    //小数点以下の長さを指定
    cout << fixed << setprecision(15) << x1 << " " << y1 << endl;
    return 0;
}