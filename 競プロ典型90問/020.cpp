// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
#include <atcoder/modint>
#include <boost/multiprecision/cpp_int.hpp>
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

namespace mp = boost::multiprecision;

mp::cpp_int f(mp::cpp_int c, mp::cpp_int b) {
    mp::cpp_int res = 1;
    while (b > 0) {
        if (b % 2 == 1) res *= c;
        c *= c;
        b /= 2;
    }
    return res;
}

int main() {
    mp::cpp_int a, b, c;
    cin >> a >> b >> c;
    if (a < f(c, b))
        cout << "Yes"
             << "\n";
    else
        cout << "No"
             << "\n";
    return 0;
}