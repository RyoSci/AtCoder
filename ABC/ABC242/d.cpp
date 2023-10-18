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
    string s;
    cin >> s;
    ll q;
    cin >> q;

    rep(i, q) {
        ll t, k;
        cin >> t >> k;
        k--;

        vector<ll> a;
        while (!(t == 0 or k == 0)) {
            a.emplace_back(k);
            t--;
            k /= 2;
        }

        ll ans;
        if (t == 0) {
            ans = s[k] - 'A';
        } else if (k == 0) {
            ans = s[0] - 'A';
            ans += t % 3;
            ans %= 3;
        }
        rep_e(k, a) {
            if (k % 2 == 0)
                ans++;
            else
                ans += 2;
            ans %= 3;
        }

        cout << char('A' + ans) << "\n";
    }

    return 0;
}