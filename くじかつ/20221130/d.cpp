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
vector<string> ans;
set<string> tt;
vector<string> s;

ll n, m;

void f(vector<ll> cnt, ll now, ll i) {
    if (i == n - 1 and now >= 0) {
        string x = "";
        rep(j, n - 1) {
            x += s[j];
            rep(k, cnt[j]) x += "_";
        }
        x += s[n - 1];
        if (tt.count(x) == 0 and x.size() >= 3 and x.size() <= 16) {
            ans.emplace_back(x);
            return;
        }
    } else if (i < n - 1 and now >= 0) {
        rep(j, now + 1) {
            vector<ll> a = cnt;
            a[i] += j;
            if (now - j >= 0) f(a, now - j, i + 1);
        }
    }
}

int main() {
    cin >> n >> m;
    s.resize(n);
    for (ll i = 0; i < n; i++) cin >> s[i];
    vector<string> t(m);
    for (ll i = 0; i < m; i++) cin >> t[i];
    rep(i, m) tt.insert(t[i]);
    ll rest = 0;
    rep(i, n) rest += s[i].size();
    do {
        vector<ll> cnt(n - 1, 1);
        ll now = 16 - rest - (n - 1);
        f(cnt, now, 0);
        if (ans.size()) {
            cout << ans[0] << "\n";
            return 0;
        }
        // for (auto a : s) cout << a << " ";
        // cout << endl;
    } while (next_permutation(s.begin(), s.end()));

    cout << -1 << "\n";
    return 0;
}