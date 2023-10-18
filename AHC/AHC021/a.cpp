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

double Randouble() { return 1.0 * rand() / RAND_MAX; }

int main() {
    clock_t start = clock();

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

    ll n = 30;
    // ll n;
    // cin >> n;

    // 入力
    vector b(n, vector(n, 0ll));
    vector<P> b_pos(n * n);

    rep(i, n) {
        rep(j, i + 1) {
            cin >> b[i][j];
            b_pos[b[i][j]] = P(i, j);
        }
    }

    // 初期盤面
    ll cnt = 0;
    vector b_best(n, vector(n, 0ll));
    vector<P> b_best_pos(n * n);
    rep(i, n) {
        rep(j, i + 1) {
            b_best[i][j] = cnt;
            b_best_pos[b_best[i][j]] = P(i, j);
            cnt++;
        }
    }

    ll best_score = 0;
    vector<tuple<ll, ll, ll, ll>> log;
    vector b_best_tmp(n, vector(n, 0ll));
    vector<P> b_best_pos_tmp(n * n);
    b_best_tmp = b_best;
    b_best_pos_tmp = b_best_pos_tmp;

    // 入力盤面を合わせながら、スコアを確認
    auto score = [&] {
        vector b_tmp(n, vector(n, 0ll));
        vector<P> b_pos_tmp(n);
        b_tmp = b;
        b_pos_tmp = b_pos;
        vector<tuple<ll, ll, ll, ll>> log_tmp;

        auto swap_pos = [&](ll i, ll j, ll ni, ll nj) {
            b_pos_tmp[b_tmp[i][j]] = P(ni, nj);
            b_pos_tmp[b_tmp[ni][nj]] = P(i, j);
            swap(b_tmp[i][j], b_tmp[ni][nj]);
            log_tmp.emplace_back(i, j, ni, nj);
        };

        // 左上から合わせていく
        rep(i, n) {
            if (timer()) break;
            rep(j, i + 1) {
                if (timer()) break;

                ll target = b_best_tmp[i][j];
                auto [pi, pj] = b_pos_tmp[target];

                while (!(i == pi and j == pj)) {
                    if (j < pj) {
                        swap_pos(pi, pj, pi, pj - 1);
                        pj--;
                    } else if (j > pj) {
                        swap_pos(pi, pj, pi, pj + 1);
                        pj++;
                    } else {
                        if (i < pi) {
                            swap_pos(pi, pj, pi - 1, pj);
                            pi--;
                        } else if (i > pi) {
                            swap_pos(pi, pj, pi + 1, pj);
                            pi++;
                        }
                    }
                    if (timer()) break;
                }
            }
        }

        ll now_score = 100000 - 5 * log_tmp.size();

        // 山登り
        if (now_score > best_score) {
            log = log_tmp;
            best_score = now_score;
            b_best = b_best_tmp;
            b_best_pos = b_best_pos_tmp;
        }

        // 焼き鈍し
        // // 温度を設定する
        double T = 30.0 - 28.0 * timer() / 2.0;
        double p = exp(min(0.0, best_score - now_score) / T);
        if (Randouble() < p) {
            log = log_tmp;
            best_score = now_score;
            b_best = b_best_tmp;
            b_best_pos = b_best_pos_tmp;
        }
    };

    while (1) {
        if (timer()) break;

        // 頂点をランダムにスワップする
        // 乱数生成
        ll i, j;
        i = rand() % n;
        j = rand() % (i + 1);
        ll ni, nj;
        ni = rand() % n;
        nj = rand() % (ni + 1);

        // チェックする
        auto check = [&](ll i, ll j, ll ni, ll nj) {
            // 上二つ
            ll i0, j0, i1, j1;
            i0 = i - 1;
            j0 = j - 1;
            i1 = i - 1;
            j1 = j;
            bool flag = true;
            if (0 <= i0 and i0 < n and 0 <= j0 and j0 < i0 + 1) {
                if (b_best_tmp[ni][nj] < b_best_tmp[i0][j0]) flag = false;
            }
            if (0 <= i1 and i1 < n and 0 <= j1 and j1 < i1 + 1) {
                if (b_best_tmp[ni][nj] < b_best_tmp[i1][j1]) flag = false;
            }
            // 下二つ
            i0 = i + 1;
            j0 = j - 1;
            i1 = i + 1;
            j1 = j;
            if (0 <= i0 and i0 < n and 0 <= j0 and j0 < i0 + 1) {
                if (b_best_tmp[ni][nj] < b_best_tmp[i0][j0]) flag = false;
            }
            if (0 <= i1 and i1 < n and 0 <= j1 and j1 < i1 + 1) {
                if (b_best_tmp[ni][nj] < b_best_tmp[i1][j1]) flag = false;
            }

            return flag;
        };

        auto swap_pos = [&](ll i, ll j, ll ni, ll nj) {
            b_best_pos_tmp[b_best_tmp[i][j]] = P(ni, nj);
            b_best_pos_tmp[b_best_tmp[ni][nj]] = P(i, j);
            swap(b_best_tmp[i][j], b_best_tmp[ni][nj]);
        };

        if (check(i, j, ni, nj) and check(ni, nj, i, j)) {
            // スワップする
            swap_pos(i, j, ni, nj);

        } else {
            continue;
        }
        if (timer()) break;

        // スコアを計算する
        score();

        // cout << best_score << "\n";
    }

    cout << min(10000, log.size()) << "\n";
    rep(i, min(10000, log.size())) {
        auto [a, b, c, d] = log[i];
        cout << a << ' ' << b << ' ' << c << ' ' << d << "\n";
    }

    return 0;
}