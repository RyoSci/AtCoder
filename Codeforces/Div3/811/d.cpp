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
    ll q;
    cin >> q;
    rep(_, q) {
        string t;
        cin >> t;
        ll n;
        cin >> n;
        vector<string> s;
        rep(i, n) {
            string si;
            cin >> si;
            s.emplace_back(si);
        }

        ll flag = 0;
        ll nflag = -1;
        vector<ll> p;

        ll m = t.size();
        vector<P> res;
        bool ans = true;

        rep(i, m) {
            rep(j, n) {
                ll ni = s[j].size();
                if (i + ni <= m) {
                    if (t.substr(i, ni) == s[j]) {
                        if (flag < i + ni and nflag < i + ni) {
                            nflag = i + ni;
                            p = {j, i};
                        }
                    }
                }
            }
            if (i == flag) {
                if (nflag == -1 or flag >= nflag) {
                    ans = false;
                    break;
                } else {
                    res.emplace_back(make_pair(p[0], p[1]));
                    flag = nflag;
                    nflag = -1;
                }
            }
        }
        if (ans) {
            cout << res.size() << "\n";
            rep_e(e, res) {
                cout << e.first + 1 << ' ' << e.second + 1 << "\n";
            }
        } else
            cout << -1 << "\n";
    }
    return 0;
}