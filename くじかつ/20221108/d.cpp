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

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> twice2once(10010010, -1);
    rep(i, 1001 + 10) { twice2once[i * i] = i; }

    vector<vector<ll>> dis(n, vector<ll>(n, INF));

    dis[0][0] = 0;
    queue<P> q;
    q.emplace(P(1, 1));
    while (q.size() > 0) {
        auto [k, l] = q.front();
        q.pop();
        rep_s(i, 1, n + 1) {
            ll j_m_l2 = m - (i - k) * (i - k);
            if (j_m_l2 >= 0 and twice2once[j_m_l2] != -1) {
                ll j = twice2once[j_m_l2] + l;
                if (1 <= j and j <= n and
                    dis[i - 1][j - 1] > dis[k - 1][l - 1] + 1) {
                    dis[i - 1][j - 1] = dis[k - 1][l - 1] + 1;
                    q.emplace(P(i, j));
                }
                j = -twice2once[j_m_l2] + l;
                if (1 <= j and j <= n and
                    dis[i - 1][j - 1] > dis[k - 1][l - 1] + 1) {
                    dis[i - 1][j - 1] = dis[k - 1][l - 1] + 1;
                    q.emplace(P(i, j));
                }
            }
        }
    }

    rep(i, n) {
        for (auto a : dis[i]) {
            if (a == INF)
                cout << -1 << " ";
            else
                cout << a << " ";
        }
        cout << endl;
    }

    return 0;
}