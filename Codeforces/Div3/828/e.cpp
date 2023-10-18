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
using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
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

// "https://qiita.com/drken/items/3beb679e54266f20ab63"

// エラトステネスの篩
struct Eratosthenes {
    // テーブル
    vector<bool> isprime;

    // 整数 i を割り切る最小の素数
    vector<int> minfactor;

    // コンストラクタで篩を回す
    Eratosthenes(int N) : isprime(N + 1, true), minfactor(N + 1, -1) {
        // 1 は予めふるい落としておく
        isprime[1] = false;
        minfactor[1] = 1;

        // 篩
        for (int p = 2; p <= N; ++p) {
            // すでに合成数であるものはスキップする
            if (!isprime[p]) continue;

            // p についての情報更新
            minfactor[p] = p;

            // p 以外の p の倍数から素数ラベルを剥奪
            for (int q = p * 2; q <= N; q += p) {
                // q は合成数なのでふるい落とす
                isprime[q] = false;

                // q は p で割り切れる旨を更新
                if (minfactor[q] == -1) minfactor[q] = p;
            }
        }
    }

    // 高速素因数分解
    // pair (素因子, 指数) の vector を返す
    vector<pair<int, int>> factorize(int n) {
        vector<pair<int, int>> res;
        while (n > 1) {
            int p = minfactor[n];
            int exp = 0;

            // n で割り切れる限り割る
            while (minfactor[n] == p) {
                n /= p;
                ++exp;
            }
            res.emplace_back(p, exp);
        }
        return res;
    }
};

int main() {
    // エラトステネスの篩
    Eratosthenes er(100000 + 1);

    ll t;
    cin >> t;
    rep(_, t) {
        ll a, b, c, d;
        cin >> a >> b >> c >> d;
        map<ll, ll> dic;

        auto pf = er.factorize(a);
        for (int i = 0; i < pf.size(); ++i) {
            dic[pf[i].first] += pf[i].second;
        }

        pf = er.factorize(b);
        for (int i = 0; i < pf.size(); ++i) {
            dic[pf[i].first] += pf[i].second;
        }

        P ans;
        ans.first = -1;
        ans.second = -1;
        rep_s(x, a + 1, c + 1) {
            pf = er.factorize(x);
            map<ll, ll> dd = dic;
            for (int i = 0; i < pf.size(); ++i) {
                dd[pf[i].first] -= pf[i].second;
                ll res = 1;
                rep_e(e, dd) {
                    auto [key, val] = e;
                    if (val > 0) res *= powl(key, val);
                }
                if ((b + 1 + res - 1) / res * res <= d) {
                    ans.first = x;
                    ans.second = (b + 1 + res - 1) / res * res;
                }
            }
        }
        cout << ans.first << ' ' << ans.second << "\n";
    }
}