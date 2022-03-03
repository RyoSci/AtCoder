#define _GLIBCXX_DEBUG
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
    string s;
    cin >> s;
    ll k;
    cin >> k;
    ll n = s.size();
    ll cnt = 0;
    rep(i, n - 1) {
        if (s[i] == s[i + 1]) cnt++;
    }

    if (cnt == n - 1) {
        cout << n * k / 2 << "\n";
    } else {
        // 1個単位
        ll tmp = 1;
        cnt = 0;
        rep(i, n - 1) {
            if (s[i] == s[i + 1])
                tmp++;
            else {
                cnt += tmp / 2;
                tmp = 1;
            }
        }
        cnt += tmp / 2;
        ll pre = 0;
        if (s[0] == s[n - 1]) {
            tmp = 1;
            ll concat = 0;
            rep_r(i, n - 1, -1) {
                if (s[i] == s[i - 1])
                    tmp++;
                else
                    break;
            }
            concat += tmp;
            pre += tmp / 2;
            tmp = 1;
            rep(i, n) {
                if (s[i] == s[i + 1])
                    tmp++;
                else
                    break;
            }
            pre += tmp / 2;
            concat += tmp;
            cout << cnt * k + (-pre + concat / 2) * (k - 1) << "\n";
        } else {
            cout << cnt * k << "\n";
        }
        return 0;
    }
}