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
    ll a, b, c;
    cin >> a >> b >> c;
    ll odd = 0;
    ll even = 0;
    if (a % 2 == 1)
        odd++;
    else
        even++;
    if (b % 2 == 1)
        odd++;
    else
        even++;
    if (c % 2 == 1)
        odd++;
    else
        even++;

    if (odd == 3 || even == 3) {
        cout << (max(max(a, b), c) * 3 - a - b - c) / 2 << "\n";
    } else {
        if (odd == 2) {
            if (a % 2 == 1) a++;
            if (b % 2 == 1) b++;
            if (c % 2 == 1) c++;
        } else {
            if (a % 2 == 0) a++;
            if (b % 2 == 0) b++;
            if (c % 2 == 0) c++;
        }
        cout << (max(max(a, b), c) * 3 - a - b - c) / 2 + 1 << "\n";
    }
    return 0;
}