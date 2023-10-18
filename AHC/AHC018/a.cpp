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
#include <unordered_map>
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

#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

struct Pos {
    ll y, x;
};

enum class Response { not_broken, broken, finish, invalid };

struct Field {
    ll N;
    ll C;
    vector<vector<ll>> is_broken;
    vector<vector<ll>> broken_cost;
    ll total_cost;

    Field(ll N, ll C)
        : N(N),
          C(C),
          is_broken(N, vector<ll>(N, 0)),
          broken_cost(N, vector<ll>(N, 0)) {}

    Response query(ll y, ll x, ll power) {
        total_cost += power + C;
        cout << y << " " << x << " " << power << endl;  // endl does flush
        ll r;
        cin >> r;
        switch (r) {
            case 0:
                return Response::not_broken;
            case 1:
                is_broken[y][x] = 1;
                return Response::broken;
            case 2:
                is_broken[y][x] = 1;
                return Response::finish;
            default:
                return Response::invalid;
        }
    }
};

struct Solver {
    ll N;
    ll C;
    vector<Pos> source_pos;
    vector<Pos> house_pos;
    Field field;
    // map<Pos, pair<Pos, ll>> graph;
    // map<pair<Pos, Pos>, ll> graph;
    // map<P, ll> graph;
    map<ll, vector<P>> graph;
    vector<Pos> all_nodes;
    vector<Pos> tmp_brokens;
    vector<ll> dy = {-1, 0, 1, 0};
    vector<ll> dx = {0, 1, 0, -1};
    ll sample_N = 10;
    ll sample_wid = N / sample_N;

    Solver(ll N, const vector<Pos>& source_pos, const vector<Pos>& house_pos,
           ll C)
        : N(N),
          source_pos(source_pos),
          house_pos(house_pos),
          C(C),
          field(N, C) {}

    void solve() {
        // 等間隔にポイントを決めて掘る 地質調査
        dig_samples();

        // 地質調査結果をグラフにする
        make_graph();

        // 各家からダイクストラ
        dijkstra();

        // should receive Response::finish and exit before entering here
        assert(false);
    }

    void dig_samples() {
        // 各水源と家も掘る
        for (Pos house : house_pos) {
            destruct(house.y, house.x);
            // all_nodes.emplace_back(house);
        }

        for (Pos source : source_pos) {
            destruct(source.y, source.x);
            // all_nodes.emplace_back(source);
        }
        // for (ll y = sample_N; y < N; y += sample_N) {
        //     for (ll x = sample_N; x < N; x += sample_N) {
        //         if (field.is_broken[y][x]) continue;
        //         destruct(y, x);
        //         Pos tmp = {y, x};
        //         all_nodes.emplace_back(tmp);
        //     }
        // }
        for (ll yi = 1; yi < sample_N; yi += 1) {
            ll y = yi * sample_wid;
            for (ll xi = 1; xi < sample_N; xi += 1) {
                ll x = xi * sample_wid;
                if (field.is_broken[y][x]) continue;
                destruct(y, x);
                Pos tmp = {y, x};
                all_nodes.emplace_back(tmp);
            }
        }
    }

    ll encode_pos(Pos a) {
        ll ret = a.y * 200 + a.x;
        return ret;
    }

    Pos decode_pos(ll a) {
        Pos ret = {a / 200, a % 200};
        return ret;
    }

    ll cal_edge_costs(Pos node, Pos nxnode) {
        ll cost = field.broken_cost[node.y][node.x];
        cost += field.broken_cost[nxnode.y][nxnode.x];
        // cost /= 2;
        cost *= (abs(node.y - nxnode.y) + abs(node.x - nxnode.x));
        return cost;
    }

    void make_ede(Pos node, Pos nxnode, ll cost) {
        graph[encode_pos(node)].emplace_back(P(encode_pos(nxnode), cost));
        graph[encode_pos(nxnode)].emplace_back(P(encode_pos(node), cost));
        return;
    }

    void make_graph() {
        // // 全点間に辺を貼った場合
        // for (Pos node : all_nodes) {
        //     for (Pos nxnode : all_nodes) {
        //         if (node.x == nxnode.x and node.y == nxnode.y)
        //             continue;
        //         ll cost = field.broken_cost[node.y][node.x];
        //         cost += field.broken_cost[nxnode.y][nxnode.x];
        //         cost /= 2;
        //         cost *= (abs(node.y - nxnode.y) +
        //                  abs(node.x - nxnode.x));
        //         cout << "# cost " << cost << endl;

        //         // graph[node] = pair(nxnode, cost);
        //         // graph[nxnode] = pair(node, cost);
        //         // graph[make_pair(node, nxnode)] = cost;
        //         // graph[make_pair(nxnode, node)] = cost;
        //         graph[P(encode_pos(node), encode_pos(nxnode))] = cost;
        //         graph[P(encode_pos(nxnode), encode_pos(node))] = cost;
        //     }
        // }

        // 上下左右に辺を張る
        for (Pos node : all_nodes) {
            rep(i, 4) {
                Pos nxnode;
                // nxnode = {node.y + dy[i] * sample_N, node.x + dx[i] *
                // sample_N}; if (nxnode.y < sample_N or N - sample_N <
                // nxnode.y) continue; if (nxnode.x < sample_N or N -
                // sample_N < nxnode.x) continue;
                nxnode = {node.y + dy[i] * sample_wid,
                          node.x + dx[i] * sample_wid};
                if (nxnode.y < sample_wid or
                    sample_wid * (sample_N - 1) < nxnode.y)
                    continue;
                if (nxnode.x < sample_wid or
                    sample_wid * (sample_N - 1) < nxnode.x)
                    continue;

                ll cost = cal_edge_costs(node, nxnode);
                cout << "# cost " << cost << endl;

                make_ede(node, nxnode, cost);
            }
        }

        // 家から近い地点に辺を張る
        for (Pos house : house_pos) {
            ll house_ll = encode_pos(house);
            vector<P> tmp_dis_vec;
            for (Pos node : all_nodes) {
                ll node_ll = encode_pos(node);
                if (house_ll == node_ll) continue;
                ll tmp_dis = abs(node.x - house.x) + abs(node.y - house.y);
                tmp_dis_vec.emplace_back(tmp_dis, node_ll);
            }
            sort(tmp_dis_vec.begin(), tmp_dis_vec.end());
            rep(i, 4) {
                Pos node = decode_pos(tmp_dis_vec[i].second);
                ll cost = cal_edge_costs(house, node);
                make_ede(house, node, cost);
            }
        }
        // 水源から近い地点に辺を張る
        for (Pos source : source_pos) {
            ll source_ll = encode_pos(source);
            vector<P> tmp_dis_vec;
            for (Pos node : all_nodes) {
                ll node_ll = encode_pos(node);
                if (source_ll == node_ll) continue;
                ll tmp_dis = abs(node.x - source.x) + abs(node.y - source.y);
                tmp_dis_vec.emplace_back(tmp_dis, node_ll);
            }
            sort(tmp_dis_vec.begin(), tmp_dis_vec.end());
            rep(i, 4) {
                Pos node = decode_pos(tmp_dis_vec[i].second);
                ll cost = cal_edge_costs(source, node);
                make_ede(source, node, cost);
            }
        }

        // // graphの出力確認
        // for (auto a : graph)
        //     cout << "# graph確認" << a.first.first << ' ' <<
        //     a.first.second
        //          << ' ' << a.second << endl;
        // cout << endl;
    }

    void dijkstra() {
        // ll broken_size = tmp_brokens.size();
        // dp[i][s][t]: =
        // i番目のスコアで、sのhomeから出発して、tのPosにいくまでの最短距離
        //       dp[k][house_pos.size()][broken_size] = INF;
        //       dp[k][0][] = 0;
        //       一旦保留

        // dp[s][t]:=s->tに向かう際の最短経路
        for (Pos house : house_pos) {
            map<ll, ll> dp;
            dp[encode_pos(house)] = 0;
            priority_queue<P> pq;
            pq.emplace(P(-dp[encode_pos(house)], encode_pos(house)));

            // 復元用
            map<ll, ll> prev;

            while (pq.size()) {
                auto [d, phouse_ll] = pq.top();
                Pos phouse = decode_pos(phouse_ll);
                pq.pop();
                d *= -1;

                if (dp.count(encode_pos(phouse)) and dp[encode_pos(phouse)] < d)
                    continue;

                // 全点間に辺を張っていた時の処理
                // for (Pos nhouse : all_nodes) {
                //     if (encode_pos(phouse) == encode_pos(nhouse))
                //     continue; ll cost = graph[P(encode_pos(phouse),
                //     encode_pos(nhouse))]; if
                //     (dp.count(encode_pos(nhouse)) == 0 or
                //         dp[encode_pos(nhouse)] >
                //             dp[encode_pos(phouse)] + cost) {
                //         dp[encode_pos(nhouse)] = dp[encode_pos(phouse)] +
                //         cost; pq.emplace(
                //             P(-dp[encode_pos(nhouse)],
                //             encode_pos(nhouse)));

                //         // 復元用
                //         prev[encode_pos(nhouse)] = encode_pos(phouse);
                //     }
                // }

                // 上下左右の点間に辺を張った時の実装
                for (auto [nhouse_ll, cost] : graph[phouse_ll]) {
                    Pos nhouse = decode_pos(nhouse_ll);
                    if (encode_pos(phouse) == encode_pos(nhouse)) continue;
                    if (dp.count(encode_pos(nhouse)) == 0 or
                        dp[encode_pos(nhouse)] >
                            dp[encode_pos(phouse)] + cost) {
                        dp[encode_pos(nhouse)] = dp[encode_pos(phouse)] + cost;
                        pq.emplace(
                            P(-dp[encode_pos(nhouse)], encode_pos(nhouse)));

                        // 復元用
                        prev[encode_pos(nhouse)] = encode_pos(phouse);
                    }
                }
            }
            // ダイクストラの復元
            // 水源地の中で最もコストが低い地点から家までバックトレースする
            Pos now = source_pos[0];
            for (Pos source : source_pos) {
                if (dp[encode_pos(now)] > dp[encode_pos(source)]) now = source;
            }

            vector<Pos> trace;
            trace.emplace_back(now);

            while (now.x != house.x or now.y != house.y) {
                now = decode_pos(prev[encode_pos(now)]);
                trace.emplace_back(now);
            }

            reverse(trace.begin(), trace.end());
            // traceの順にmoveしながら掘っていく、併せて辺のコストも更新する
            cout << "# ダイクストラの結果を掘る" << trace.size() << endl;
            rep(i, trace.size() - 1) {
                move(trace[i], trace[i + 1]);
                make_ede(trace[i], trace[i + 1], 0);
            }
        }
    }

    void move(Pos start, Pos goal) {
        // you can output comment
        cout << "# move from (" << start.y << "," << start.x << ") to ("
             << goal.y << "," << goal.x << ")" << endl;

        // down/up
        if (start.y < goal.y) {
            for (ll y = start.y; y < goal.y; y++) {
                destruct(y, start.x);
            }
        } else {
            for (ll y = start.y; y > goal.y; y--) {
                destruct(y, start.x);
            }
        }

        // right/left
        if (start.x < goal.x) {
            for (ll x = start.x; x <= goal.x; x++) {
                destruct(goal.y, x);
            }
        } else {
            for (ll x = start.x; x >= goal.x; x--) {
                destruct(goal.y, x);
            }
        }
    }

    void destruct(ll y, ll x) {
        // excavate (y, x) with fixed power until destruction
        ll power = 100;
        if (C <= 8)
            power = 20;
        else if (C <= 32)
            power = 60; 
        else if (C <= 64)
            power = 120;
        else if (C <= 128)
            power = 400;

        ll cnt = 0;
        while (!field.is_broken[y][x]) {
            Response result = field.query(y, x, power);
            if (result == Response::finish) {
                // cerr << "total_cost=" << field.total_cost << endl;
                exit(0);
            } else if (result == Response::invalid) {
                cerr << "invalid: y=" << y << " x=" << x << endl;
                exit(1);
            }
            // 壊れるまでにかかったコストを記録する
            field.broken_cost[y][x] += power + C;
        }
    }
};

int main() {
    ll N, W, K, C;
    cin >> N >> W >> K >> C;
    vector<Pos> source_pos(W);
    vector<Pos> house_pos(K);
    for (ll i = 0; i < W; i++) {
        cin >> source_pos[i].y >> source_pos[i].x;
    }
    for (ll i = 0; i < K; i++) {
        cin >> house_pos[i].y >> house_pos[i].x;
    }

    Solver solver(N, source_pos, house_pos, C);
    solver.solve();
}
