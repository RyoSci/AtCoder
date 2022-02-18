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
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)
// #include <atcoder/all>
// #include <atcoder/modint>
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;

ll gcd(ll a, ll b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> a(n);
    set<ll> power_2;
    for (ll i = 0; i < n; i++) {
        cin >> a[i];
        a[i] /= 2;
        ll now = 2;
        rep(j, 60) {
            if (a[i] % now == 0) {
                now *= 2;
            } else {
                power_2.insert(now / 2);
                break;
            }
        }
    }

    if (power_2.size() > 1) {
        cout << 0 << "\n";
    } else {
        ll syokou = 1;
        rep(i, n) { syokou = lcm(syokou, a[i]); }
        // ll kousa = syokou * 2;
        if (m >= syokou && syoukou > 0)
            cout << (m - syokou) / (syokou * 2) + 1 << "\n";
        else
            cout << 0 << "\n";
    }
    return 0;
}