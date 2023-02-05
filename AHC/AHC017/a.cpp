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
// #define INF 100000000
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

double Randouble() { return 1.0 * rand() / RAND_MAX; }

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

    // 出力変数
    vector<ll> ansr(m, d);
    double ans = 0.0;

    // i日目に使えない道を管理する
    // vector<set<ll>> stops(d);
    vector stops(d, vector(m, false));

    // 距離を求める関数
    auto dijkstra = [&](ll day, vector<vector<ll>>& dis) {
        rep(par, n) {
            priority_queue<P> pq;
            pq.emplace(P(-dis[par][par], par));
            while (pq.size()) {
                auto [tmpd, node] = pq.top();
                pq.pop();
                tmpd *= -1;
                if (dis[par][node] < tmpd) continue;
                for (auto [to, w, i] : g[node]) {
                    // if (day != -1 and stops[day].count(i)) continue;
                    if (day != -1 and stops[day][i]) continue;
                    if (dis[par][to] > dis[par][node] + w) {
                        dis[par][to] = dis[par][node] + w;
                        pq.emplace(P(-dis[par][to], to));
                    }
                }
            }
        }
    };

    ll INF = 1000000000;
    // 各点間の最短距離を求めておく
    vector dis_min(n, vector(n, INF));
    rep(i, n) dis_min[i][i] = 0;
    dijkstra(-1, dis_min);

    // 時間になったら出る関数
    auto timer = [&]() {
        clock_t end = clock();
        const double time =
            static_cast<double>(end - start) / CLOCKS_PER_SEC * 1.0;  // sec
        if (time > 5.0)
            return true;
        else
            return false;
    };

    // 中心からkk個ずつのグループにしていく
    // 500,500に近い座標を調べる
    ll center;
    center = 0;
    ll distmp = INF;
    rep(i, n) {
        ll tmp = (x[i] - 500) * (x[i] - 500) + (y[i] - 500) * (y[i] - 500);
        if (distmp > tmp) {
            distmp = tmp;
            center = i;
        }
    }

    // 中心からdfs, bfsでエリア分割を試す
    rep(i, 2) {
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

        auto dfs = [&](auto dfs, ll u) -> void {
            for (auto [v, w, i] : g[u]) {
                if (seen[i]) continue;
                seen[i] = 1;
                now++;
                if (now == d) {
                    now = 0;
                    areaid++;
                }
                areas[areaid].emplace_back(i);
                dfs(dfs, v);
            }
        };

        if (i % 2)
            bfs();
        else
            dfs(dfs, 0);

        // 各エリアの頂点をシャッフルする
        mt19937 get_rand_mt;
        rep(i, kk + 1) {
            shuffle(areas[i].begin(), areas[i].end(), get_rand_mt);
        }

        // d日間各エリアからそれぞれ 1ずつ合計m+d-1/d ずつ取っていく
        vector<ll> r(m, d);
        rep(i, d + 10) {
            rep(j, kk) {
                if (areas[j].size() > i) {
                    r[areas[j][i]] = i + 1;
                }
            }
        }

        if (i % 2 == 0) ansr = r;

        // 各日にちごとに計算する
        auto f = [&](ll day) {
            vector dis(n, vector(n, INF));
            rep(i, n) dis[i][i] = 0;
            dijkstra(day, dis);
            double res = 0.0;
            rep(i, n) rep(j, n) res += dis[i][j] - dis_min[i][j];
            return res / (n * (n - 1));
        };

        // スコア関数を作成する
        auto score = [&]() {
            // 通行止め管理
            // stops.clear();
            // rep(i, m) stops[r[i] - 1].insert(i);
            rep(i, d) rep(j, m) stops[i][j] = false;
            rep(i, m) stops[r[i] - 1][i] = true;

            // 日にちごとにまとめる
            double res = 0.0;
            rep(day, d) {
                res += f(day);
                if (timer()) break;
            }
            return round(1000.0 * res / d);
        };

        if (timer()) break;

        double current_score = score();
        if (timer()) break;

        if (ans < current_score) {
            ansr = r;
            ans = current_score;
        }

        if (timer()) break;

        //     // 焼きなましを実施していく
        //     while (1) {
        //         if(timer()) break;
        //         // 乱数生成
        //         ll i, j;
        //         i = rand() % m;
        //         j = rand() % m * rand() % m;
        //         j %= m;
        //         // スワップする
        //         swap(r[i], r[j]);

        //         // socreを計算する
        //         double now_score = score();
        //         // // 温度を設定する
        //         double T = 30.0 - 28.0 * time / 6.0;
        //         double p = exp(min(0.0, current_score - now_score) / T);
        //         // 小数点以下の長さを指定
        //         cout << fixed << setprecision(15) << p << endl;
        //         if (Randouble() < p) {
        //             current_score = now_score;
        //         } else
        //             swap(r[i], r[j]);

        //         // // 山登り
        //         // if (now_score > current_score) {
        //         //     current_score = now_score;
        //         // } else
        //         //     swap(r[i], r[j]);
        //     }
    }

    for (auto a : ansr) cout << a << " ";
    cout << endl;
    return 0;
}