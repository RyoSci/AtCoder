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

void chmin(&x, y){
    if (x > y) x = y;
    return;
}

int main()
{
    ll n, m, r;
    cin >> n >> m >> R;
    vector<ll> r(R);
    for (ll i = 0; i < R; i++) cin >> r[i];
    vector<vector<P>> g(n);
    rep(i,m){
        ll a, b, c;
        cin >> a >> b >> c;
        a--;
        b--;
        g[a].emplace_back(make_pair(b, c));
        g[b].emplace_back(make_pair(a, c));
    }

    rep(i,n){
    vector<vector<ll>> dp(1<<R, vector<ll>(n, INF));
    ll flag = -1;
    rep(j, R) {
        if (r[j]-1==i){
            flag = j;
        }
    }
    if (flag != -1) dp[1 << flag][i] = 0;
    else
        dp[0][i] = 0;
    
    rep(i,1<<)
    }

    

    ll ans = INF;
    rep(i, n) chmin(ans, dp[1 << R][i]);
    cout << ans << "\n";

    return 0;
}