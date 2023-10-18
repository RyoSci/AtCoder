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
    ll n;
    cin >> n;
    vector<ll> p(n);
    for (ll i = 0; i < n; i++) cin >> p[i];

    ll change_i;
    rep_r(i, n - 1, 0) {
        if (p[i - 1] > p[i]) {
            change_i = i - 1;
            break;
        }
    }

    ll change_j, change_j_num = 0;

    rep_s(i, change_i + 1, n) {
        if (p[i] < p[change_i] and p[i] > change_j_num) {
            change_j = i;
            change_j_num = p[i];
        }
    }

    swap(p[change_i], p[change_j]);

    vector<ll> a, b;

    rep(i, change_i + 1) a.emplace_back(p[i]);
    rep_s(i, change_i + 1, n) b.emplace_back(p[i]);
    sort(b.rbegin(), b.rend());

    for (auto a : a) cout << a << " ";
    for (auto a : b) cout << a << " ";
    cout << endl;
    return 0;
}