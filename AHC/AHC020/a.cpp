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

void chmax(ll &x, ll y) {
    x = max(x, y);
    return;
}

double Randouble() { return 1.0 * rand() / RAND_MAX; }

int main() {
    clock_t start = clock();

    // 入力受け取り
    ll N, M, K;
    cin >> N >> M >> K;

    vector<ll> x(N, 0), y(N, 0);
    rep(i, N) cin >> x[i] >> y[i];

    vector<ll> u(M, 0), v(M, 0), w(M, 0);
    vector<vector<T>> g(N);
    rep(i, M) {
        cin >> u[i] >> v[i] >> w[i];
        u[i]--;
        v[i]--;
        g[u[i]].emplace_back(v[i], w[i], i);
        g[v[i]].emplace_back(u[i], w[i], i);
    }

    vector<ll> a(K, 0), b(K, 0);
    rep(i, K) cin >> a[i] >> b[i];

    // 集合の0と各点間の距離の最短距離を求める
    // vector dis_base2base(N, vector(N, INF));
    // rep(i, M) {
    //     dis_base2base[u[i]][v[i]] = w[i];
    //     dis_base2base[v[i]][u[i]] = w[i];
    // }
    // rep(i, N) dis_base2base[i][i] = 0;

    vector<ll> dis_one2base(N, INF);
    dis_one2base[0] = 0;
    vector<P> pre_base(N);

    priority_queue<P> pq;
    pq.emplace(0, 0);
    while (pq.size()) {
        auto [d, par] = pq.top();
        pq.pop();
        d *= -1;

        if (dis_one2base[par] < d) continue;
        for (auto [chi, wj, j] : g[par]) {
            if (dis_one2base[chi] > d + wj) {
                dis_one2base[chi] = d + wj;
                pq.emplace(-(d + wj), chi);
                pre_base[chi] = P(j, par);
            }
        }
    }
    // 各家から放送基地局との距離を求めて照準に並べる
    vector<vector<P>> dis_home2base(K);
    rep(i, K) {
        rep(j, N) {
            ll d =
                (a[i] - x[j]) * (a[i] - x[j]) + (b[i] - y[j]) * (b[i] - y[j]);
            if (d <= 5000 * 5000) dis_home2base[i].emplace_back(d, j);
        }
        sort(dis_home2base[i].begin(), dis_home2base[i].end());
    }

    // 時間になったら出る関数
    auto timer = [&]() {
        clock_t end = clock();
        const double time =
            static_cast<double>(end - start) / CLOCKS_PER_SEC * 1.0;  // sec
        if (time > 1.9)
            return true;
        else
            return false;
    };

    // 選ぶ頂点をランダムにする
    // 各放送基地局の担当の最大距離
    vector<ll> dis_max_base2home_ans(N, 0);
    // V'を形成するための辺集合を求める
    vector<ll> Ed_ans(M, 0);
    double score_ans = 0.0;
    bool flag = true;
    ll ii = 0;
    // V'の点集合
    vector<ll> Vd(N, 0);

    // 各放送基地局の担当の最大距離
    vector<ll> dis_max_base2home(N, 0);
    // まずは各家から最も距離が近い放送基地局の集合をV’とする
    vector<ll> dis_rank(K, 0);
    // V'を形成するための辺集合を求める
    vector<ll> Ed(M, 0);

    while (1) {
        if (flag) {
            rep(i, K) {
                if (timer()) break;
                ll tmp = 0;
                dis_rank[i] = tmp;
                ll j = dis_home2base[i][tmp].second;
                Vd[j]++;
            }
            flag = false;
        } else {
            if (timer()) break;

            // リセットする
            dis_rank[ii] = 0;
            ll j = dis_home2base[ii][0].second;
            Vd[j]--;

            ll tmp = rand();
            tmp %= dis_home2base[ii].size();
            tmp %= 10;
            dis_rank[ii] = tmp;
            j = dis_home2base[ii][tmp].second;
            Vd[j]++;

            ii++;
        }
        if (timer()) break;

        rep(i, N) {
            if (Vd[i] == 0) continue;
            ll now_node = i;
            while (1) {
                if (timer()) break;
                ll edgej = pre_base[now_node].first;
                now_node = pre_base[now_node].second;
                Ed[edgej] = 1;
                if (now_node == 0) break;
            }
            if (timer()) break;
        }
        if (timer()) break;

        // 各放送基地局の担当の最大の距離までPを減らす
        rep(i, K) {
            if (timer()) break;
            auto [d, j] = dis_home2base[i][dis_rank[i]];
            chmax(dis_max_base2home[j], d);
        }
        if (timer()) break;

        rep(i, N) {
            if (timer()) break;
            dis_max_base2home[i] = ll(ceil(sqrt(dis_max_base2home[i])));
        }
        // rep(i, N) {
        //     dis_max_base2home[i] = ll(round(sqrt(dis_max_base2home[i]) +
        //     0.5));
        // }
        if (timer()) break;

        // スコアを求める
        ll S = 0;
        for (auto a : dis_max_base2home) S += a * a;
        rep(i, M) if (Ed[i]) S += w[i];
        auto score = [&]() -> double {
            double res = round(1e6 * (1.0 + 1e8 / (double(S) + 1e7)));
            return res;
        };

        double score_now = score();
        // if (score_ans < score_now) {
        //     score_ans = score_now;
        //     dis_max_base2home_ans = dis_max_base2home;
        //     Ed_ans = Ed;
        // }

        if (timer()) break;

        // // 温度を設定する
        double T = 30.0 - 28.0 * timer() / 2.0;
        double p = exp(min(0.0, score_ans - score_now) / T);
        if (Randouble() < p) {
            score_ans = score_now;
            dis_max_base2home_ans = dis_max_base2home;
            Ed_ans = Ed;
        } else {
            dis_max_base2home = dis_max_base2home_ans;
            Ed = Ed_ans;
        }

        // // 山登り
        // if (score_now > score_ans) {
        //     score_ans = score_now;
        //     dis_max_base2home_ans = dis_max_base2home;
        //     Ed_ans = Ed;
        // } else {
        //     dis_max_base2home = dis_max_base2home_ans;
        //     Ed = Ed_ans;
        // }
        if (timer()) break;

        // 小数点以下の長さを指定
        cout << fixed << setprecision(15) << score_ans << endl;
    }

    // 出力する
    for (auto a : dis_max_base2home_ans) cout << a << " ";
    cout << endl;
    for (auto a : Ed_ans) cout << a << " ";
    cout << endl;

    return 0;
}
