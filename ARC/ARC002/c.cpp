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
    ll n;
    cin >> n;
    string s;
    cin >> s;
    s += "Z";
    vector<string> sc;
    rep_e(c, "ABXY") {
        rep_e(d, "ABXY") {
            string tmp = "";
            tmp += c;
            tmp += d;
            sc.push_back(tmp);
        }
    }
    ll ans = INF;
    ll m = sc.size();
    rep(i, m) {
        string l = sc[i];
        rep(j, m) {
            string r = sc[j];
            // 数える
            string tmp = "";
            rep(i, s.length() - 1) {
                if (s.substr(i, 2) == l) {
                    tmp += "l";
                    i += 1;
                } else
                    tmp += s[i];
            }
            tmp += "Z";
            string tmp1 = "";
            rep(i, tmp.length() - 1) {
                if (tmp.substr(i, 2) == r) {
                    tmp1 += "r";
                    i += 1;
                } else
                    tmp1 += tmp[i];
            }
            ans = min(ans, tmp1.length());
            // cout << ans << ' ' << tmp << ' ' << tmp1 << "\n";
        }
    }
    cout << ans << "\n";
    return 0;
}