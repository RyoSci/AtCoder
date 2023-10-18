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
using lli = long long;
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
        string a, b;
        cin >> a >> b;
        ll n, m;
        n = a.size();
        m = b.size();
        string ans;
        if (a[n - 1] == 'S') {
            if (b[m - 1] == 'S') {
                if (n > m)
                    ans = "<";
                else if (n == m)
                    ans = "=";
                else
                    ans = ">";
            } else
                ans = "<";
        } else if (a[n - 1] == 'M') {
            if (b[m - 1] == 'S')
                ans = ">";
            else if (b[m - 1] == 'M')
                ans = "=";
            else
                ans = "<";
        }
        if (a[n - 1] == 'L') {
            if (b[m - 1] == 'L') {
                if (n > m)
                    ans = ">";
                else if (n == m)
                    ans = "=";
                else
                    ans = "<";
            } else
                ans = ">";
        }
        cout << ans << "\n";
    }
    return 0;
}