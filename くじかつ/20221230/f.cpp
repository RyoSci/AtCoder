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

int main() {
    ll m, k;
    cin >> m >> k;
    if (m == 1) {
        if (k != 0)
            cout << -1 << "\n";
        else
            cout << 0 << ' ' << 0 << ' ' << 1 << ' ' << 1 << "\n";
    } else {
        if (0 <= k and k < (1LL << m)) {
            deque<ll> ans;
            ans.emplace_back(k);
            rep(i, 1LL << m) {
                if (i == k) continue;
                ans.emplace_back(i);
                ans.emplace_front(i);
            }
            ans.emplace_front(k);
            for (auto a : ans) cout << a << " ";
            cout << endl;
        } else
            cout << -1 << "\n";
    }
    return 0;
}