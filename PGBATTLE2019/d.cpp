// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
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
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll N, M, T, K;
    cin >> N >> M >> T >> K;
    vector<vector<tuple<ll, ll, ll>>> g(N);
    rep(i, M) {
        ll a, b, c, d;
        cin >> a >> b >> c >> d;
        a--;
        b--;
        g[a].push_back(make_tuple(b, c, d));
        g[b].push_back(make_tuple(a, c, d));
    }
    vector<ll> costs(N, INF);
    costs[0] = 0;
    priority_queue<P> q;
    q.push(make_pair(-costs[0], 0));
    while (!q.empty()) {
        auto [t, a] = q.top();
        q.pop();
        t = -t;
        if (costs[a] < t) continue;
        rep_e(chi, g[a]) {
            auto [b, c, d] = chi;

            ll tt;
            // 時間によって処理を分岐する
            if (t + c <= T) {
                // 通れるなら通るのが最善
                // 条件に入れる時間tは到着時間を入れる
                if (d - (T - (t + c)) <= K) {
                    if (costs[b] > t + c) {
                        costs[b] = t + c;
                        q.push(make_pair(-costs[b], b));
                    }
                }
                // 混雑度が単調減少するまで待つ
                else {
                    tt = T + d - K;
                    if (costs[b] > tt + c) {
                        costs[b] = tt + c;
                        q.push(make_pair(-costs[b], b));
                    }
                }
            } else if (t <= T && T <= t + c) {
                // 通れるなら通るのが最善
                // 条件に入れる時間tは最大値を入れる
                if (d - (T - T) <= K) {
                    if (costs[b] > t + c) {
                        costs[b] = t + c;
                        q.push(make_pair(-costs[b], b));
                    }
                }
                // 混雑度が単調減少するまで待つ
                else {
                    tt = T + d - K;
                    if (costs[b] > tt + c) {
                        costs[b] = tt + c;
                        q.push(make_pair(-costs[b], b));
                    }
                }

            } else {
                // 通れるなら通るのが最善
                // 条件に入れる時間tは出発時間を入れる
                if (d + (T - t) <= K) {
                    if (costs[b] > t + c) {
                        costs[b] = t + c;
                        q.push(make_pair(-costs[b], b));
                    }
                }
                // 混雑度が単調減少するまで待つ
                else {
                    tt = T + d - K;
                    if (costs[b] > tt + c) {
                        costs[b] = tt + c;
                        q.push(make_pair(-costs[b], b));
                    }
                }
            }
        }
    }

    if (costs[N - 1] == INF)
        cout << -1 << "\n";
    else
        cout << costs[N - 1] << "\n";

    return 0;
}