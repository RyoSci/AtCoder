// #define _GLIBCXX_DEBUG
#include <time.h>

#include <algorithm>
#include <atcoder/all>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <random>
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
    clock_t start = clock();
    // 入力
    ll n, m, d, k;
    cin >> n >> m >> d >> k;
    vector<vector<T>> g(n);
    rep(i, m) {
        ll u, v, w;
        cin >> u >> v >> w;
        u--;
        v--;
        g[u].emplace_back(T(v, w, i));
        g[v].emplace_back(T(u, w, i));
    }
    vector<ll> x(n), y(n);
    rep(i, n) cin >> x[i] >> y[i];

    // 辺をd日間、kk個のエリアに分割する
    // １日あたりの辺数は kk = m+d-1/d
    ll kk = (m + d - 1) / d;

    // 中心からkk個ずつのグループにしていく
    // 500,500に近い座標を調べる
    ll center;
    ll dis = INF;
    rep(i, n) {
        ll tmp = (x[i] - 500) * (x[i] - 500) + (y[i] - 500) * (y[i] - 500);
        if (dis > tmp) {
            dis = tmp;
            center = i;
        }
    }

    // 中心からdfs, bfsでエリア分割を試す
    ll now = 0;
    vector<vector<ll>> areas(kk + 1);
    vector<ll> seen(m, 0);
    ll areaid = 0;

    auto bfs = [&]() {
        queue<ll> q;
        q.emplace(center);
        while (q.size()) {
            ll u = q.front();
            q.pop();

            for (auto [v, w, i] : g[u]) {
                if (seen[i]) continue;
                seen[i] = 1;
                now++;
                if (now == d) {
                    now = 0;
                    areaid++;
                }
                areas[areaid].emplace_back(i);
                q.emplace(v);
            }
        }
    };

    bfs();

    // 各エリアの頂点をシャッフルする
    // 64bit版メルセンヌ・ツイスタ
    mt19937 get_rand_mt;
    rep(i, kk + 1) { shuffle(areas[i].begin(), areas[i].end(), get_rand_mt); }

    // d日間各エリアからそれぞれ 1ずつ合計m+d-1/d ずつ取っていく
    vector<ll> r(m, d);

    rep(i, d + 10) {
        rep(j, kk) {
            if (areas[j].size() > i) {
                r[areas[j][i]] = i + 1;
            }
        }
    }

    clock_t end = clock();

    // const double time =
    //     static_cast<double>(end - start) / CLOCKS_PER_SEC * 1.0;  // sec

    // cout << time << "\n";

    // 焼きなましを実施していく

    for (auto a : r) cout << a << " ";
    cout << endl;
    return 0;
}