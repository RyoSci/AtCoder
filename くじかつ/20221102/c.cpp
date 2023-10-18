// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
#include <atcoder/modint>
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
using mint = modint1000000007;
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
    ll n, m;
    cin >> n >> m;
    vector<ll> s;
    vector<char> c;

    rep(i, m) {
        ll si;
        char ci;
        cin >> si >> ci;
        s.emplace_back(si);
        c.emplace_back(ci);
    }

    rep(i, 1000) {
        string tmp = to_string(i);
        if (tmp.length() != n) continue;
        bool flag = true;
        rep(j, m) {
            if (s[j] - 1 < tmp.size() and tmp[s[j] - 1] == c[j]) {
                continue;
            } else {
                flag = false;
            }
        }
        if (flag) {
            cout << i << "\n";
            return 0;
        }
    }
    cout << -1 << "\n";
    return 0;
}