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
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll t;
    cin >> t;
    rep(_, t) {
        ll n;
        cin >> n;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        vector<ll> b(10, 0);
        rep(i, n) { b[a[i] % 10]++; }
        bool ans = false;
        rep(i, 10) rep(j, 10) rep(k, 10) {
            if ((i + j + k) % 10 == 3) {
                if (i == j && j == k) {
                    if (b[i] >= 3) ans = true;
                } else if (i == j) {
                    if (b[i] >= 2 && b[k] >= 1) ans = true;
                } else if (i != j && j != k && k != i) {
                    if (b[i] * b[j] * b[k] >= 1) ans = true;
                }
            }
            if (ans) break;
        }
        cout << (ans ? "YES" : "NO") << "\n";
    }
    return 0;
}