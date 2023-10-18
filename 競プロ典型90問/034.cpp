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
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];

    ll ans = 0;
    map<ll, ll> d;
    ll j = 0;
    rep(i, n) {
        j = max(j, i);
        while (j < n) {
            if (d.size() == k) {
                if (d.count(a[j]))
                    d[a[j]]++;
                else {
                    break;
                }
            } else {
                d[a[j]] += 1;
            }
            j++;
        }
        ans = max(ans, j - i);
        d[a[i]]--;
        if (d[a[i]] == 0) d.erase(a[i]);
    }
    cout << ans << "\n";
    return 0;
}