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
        string s, t;
        cin >> s >> t;
        vector<ll> sa, sc, ta, tc;
        vector<ll> scnt(3, 0), tcnt(3, 0);

        rep(i, n) {
            if (s[i] == 'a') {
                scnt[0]++;
                sa.emplace_back(i);
            } else if (s[i] == 'b') {
                scnt[1]++;
            } else {
                scnt[2]++;
                sc.emplace_back(i);
            }
        }
        rep(i, n) {
            if (t[i] == 'a') {
                tcnt[0]++;
                ta.emplace_back(i);
            } else if (t[i] == 'b') {
                tcnt[1]++;
            } else {
                tcnt[2]++;
                tc.emplace_back(i);
            }
        }

        if (scnt != tcnt) {
            cout << "NO"
                 << "\n";
            continue;
        }

        bool flag = true;
        rep(i, scnt[0]) {
            if (sa[i] == ta[i])
                continue;
            else if (sa[i] < ta[i]) {
                rep_s(j, sa[i] + 1, ta[i] + 1) {
                    if (s[j] == 'c') flag = false;
                }
            } else
                flag = false;
        }
        rep(i, scnt[2]) {
            if (sc[i] == tc[i])
                continue;
            else if (sc[i] > tc[i]) {
                rep_s(j, tc[i], sc[i]) {
                    if (s[j] == 'a') flag = false;
                }
            } else
                flag = false;
        }

        if (flag and scnt == tcnt)
            cout << "YES"
                 << "\n";
        else
            cout << "NO"
                 << "\n";
    }
    return 0;
}