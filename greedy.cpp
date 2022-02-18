// #include <algorithm>
// #include <cmath>
// #include <cstdio>
// #include <iomanip>
// #include <iostream>
// #include <map>
// #include <queue>
// #include <set>
// #include <stack>
// #include <string>
// #include <vector>
// using namespace std;
// #define MOD 1000000007
// #define INF (1 << 29)
// #define EPS (1e-10)
// typedef long long ll;
// typedef pair<ll, ll> P;
// #define max(x, y) ((x) > (y) ? (x) : (y))
// #define min(x, y) ((x) < (y) ? (x) : (y))
// #define rep(i, n) for (ll i = 0; i < n; i++)
// #define rep_r(i, k, n) for (ll i = k; i > n; i--)
// #define rep_s(i, k, n) for (ll i = k; i < n; i++)
// #define rep_e(c, s) for (auto c : s)
// // #include <atcoder/all>
// // #include <atcoder/modint>
// // using namespace atcoder;
// // using lli = long long;
// // using mint = modint1000000007;
// // using mint = modint998244353;

// ll gcd(ll a, ll b) {
//     if (b == 0) return a;
//     return gcd(b, a % b);
// }

// ll lcm(ll a, ll b) { return a * b / gcd(a, b); }

// int main() {
//     ll n, m;
//     cin >> n >> m;
//     vector<ll> a(n);
//     for (ll i = 0; i < n; i++) {
//         cin >> a[i];
//         a[i] /= 2;
//     }
//     ll ans = 0;
//     rep_s(x, 1, m + 1) {
//         bool flag = true;
//         rep(i, n) {
//             if (x % a[i] == 0) {
//                 ll p2 = x / a[i] - 1;
//                 if (p2 % 2 == 0 && 0 <= p2 / 2)
//                     continue;
//                 else
//                     flag = false;
//             } else
//                 flag = false;
//         }
//         if (flag) ans++;
//     }
//     cout << ans << "\n";
//     return 0;
// }
#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }
ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }

int f(int x) {
    int res = 0;
    while (x % 2 == 0) {
        x /= 2;
        res++;
    }
    return res;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    rep(i, n) cin >> a[i];

    // a -> a'
    rep(i, n) {
        if (a[i] % 2 == 1) {
            cout << 0 << endl;
            return 0;
        }
        a[i] /= 2;
    }

    // a' -> a''
    int t = f(a[0]);
    rep(i, n) {
        if (f(a[i]) != t) {
            cout << 0 << endl;
            return 0;
        }
        a[i] >>= t;  // a[i] /= 2^t
    }
    m >>= t;

    ll l = 1;
    rep(i, n) {
        l = lcm(l, a[i]);
        if (l > m) {
            cout << 0 << endl;
            return 0;
        }
    }

    m /= l;
    int ans = (m + 1) / 2;
    cout << ans << endl;
    return 0;
}