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
        ll n;
        cin >> n;
        string s;
        cin >> s;
        vector<ll> a;

        rep(i, n) {
            ll change_val;
            if (s[i] == 'L') {
                change_val = n - 1 - i - i;
            } else {
                change_val = i - (n - 1 - i);
            }
            a.emplace_back(change_val);
        }
        sort(a.rbegin(), a.rend());

        ll cnt = 0;
        rep(i, n) {
            if (s[i] == 'L') {
                cnt += i;
            } else {
                cnt += n - 1 - i;
            }
        }

        vector<ll> ans(n, 0);
        rep(i, n) {
            if (a[i] > 0) cnt += a[i];
            ans[i] = cnt;
        }
        for (auto a : ans) cout << a << " ";
        cout << endl;
    }
    return 0;
}