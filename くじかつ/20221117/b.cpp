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

ll n, m;
vector<vector<ll>> ans;

void dfs(ll i, ll pre, vector<ll> now) {
    if (i == n) {
        ans.emplace_back(now);
        return;
    }
    rep_s(j, pre + 1, m + 1) {
        vector<ll> nxt = now;
        nxt.emplace_back(j);
        dfs(i + 1, j, nxt);
    }
}

int main() {
    cin >> n >> m;
    dfs(0, 0, {});

    rep_e(e, ans) {
        for (auto a : e) cout << a << " ";
        cout << endl;
    }

    return 0;
}