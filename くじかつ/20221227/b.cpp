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
    double a, b, h, m;
    cin >> a >> b >> h >> m;
    double pi = acos(-1);
    double alpha = (h + m / 60.0) / 12.0 * 2.0 * pi;
    double beta = m / 60.0 * 2.0 * pi;
    double sita = alpha - beta;

    double c = sqrt(a * a + b * b - 2.0 * a * b * cos(sita));
    //小数点以下の長さを指定
    cout << fixed << setprecision(15) << c << endl;
    return 0;
}