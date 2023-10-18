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
    ll q;
    cin >> q;
    queue<ll> order;
    priority_queue<ll> pq;
    rep(i, q) {
        ll n;
        cin >> n;
        if (n == 1) {
            ll x;
            cin >> x;
            order.emplace(x);
        } else if (n == 2) {
            if (pq.size() > 0) {
                cout << -pq.top() << "\n";
                pq.pop();
            } else {
                cout << order.front() << "\n";
                order.pop();
            }
        } else if (n == 3) {
            while (order.size() > 0) {
                ll tmp = order.front();
                order.pop();
                pq.emplace(-tmp);
            }
        }
    }
    return 0;
}