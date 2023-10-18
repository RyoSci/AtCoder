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
    ll aa, bb, cc;
    cin >> aa >> bb >> cc;
    ll ans = -1;
    vector<ll> abc(3);
    abc = {aa, bb, cc};
    sort(abc.begin(), abc.end());
    ll a = abc[0];
    ll b = abc[1];
    ll c = abc[2];

    if (a == b and b == c and c == a)
        ans = a;
    else if (b == c)
        ans = b - a + a;
    else if (a == b) {
        if (a * 2 >= c) {
            ans = c;
        }
    } else {
        ll tmp = b - a;
        ans = tmp;
        b = b - tmp;
        c = c - tmp;
        if (a * 2 >= c) {
            ans += c;
        } else
            ans = -1;
    }
    cout << ans << "\n";
    return 0;
}