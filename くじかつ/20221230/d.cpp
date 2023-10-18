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

ll ans = 0;

vector<ll> mid(55, 0);
vector<ll> rr(55, 0);
vector<ll> cnt(55, 0);

void cal(ll i, ll rest) {
    if (i == 0)
        ans++;
    else if (rest == 1)
        return;
    else if (rest < mid[i])
        cal(i - 1, rest - 1);
    else if (rest == mid[i])
        ans += cnt[i - 1] + 1;
    else if (rest < rr[i]) {
        ans += cnt[i - 1] + 1;
        cal(i - 1, rest - mid[i]);
    } else if (rest == rr[i])
        ans += 2 * cnt[i - 1] + 1;
}

int main() {
    ll n, k;
    cin >> n >> k;
    mid[0] = 1;
    rr[0] = 1;
    cnt[0] = 1;
    rep(i, 54) mid[i + 1] = mid[i] * 2 + 1;
    rep(i, 54) rr[i + 1] = rr[i] * 2 + 3;
    rep(i, 54) cnt[i + 1] = cnt[i] * 2 + 1;

    cal(n, k);
    cout << ans << "\n";
    return 0;
}