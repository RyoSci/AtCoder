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
using namespace boost::multiprecision;
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

cpp_int gcd(cpp_int a, cpp_int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

cpp_int lcm(cpp_int a, cpp_int b) { return a / gcd(a, b) * b; }

int main() {
    cpp_int a, b;
    cin >> a >> b;
    cpp_int l = lcm(a, b);
    cpp_int m = 1000000000000000000;
    if (l > m)
        cout << "Large"
             << "\n";
    else
        cout << l << "\n";
    return 0;
}