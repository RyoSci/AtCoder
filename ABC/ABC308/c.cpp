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

// https://atcoder.jp/contests/abc308/submissions/43100273
// 有理数クラス
class Fraction {
   public:
    // @param numerator 分子
    // @param denominator 分母
    // @param reduce 通分するか(default: false), 通分する場合は計算量: O(log
    // min(num, den))
    Fraction(const long long numerator, const long long denominator,
             const bool reduce = false)
        : n_(numerator), d_(denominator), reduce_(reduce) {
        // 分母 >= 0にする(比較演算子で不等号の向きが変わらないようにするため)
        if (denominator == 0) {
            n_ = 1;
            d_ = 0;
            return;
        } else if (denominator < 0) {
            n_ = -numerator;
            d_ = -denominator;
        }

        if (reduce) {
            long long g = gcd(abs(n_), d_);

            n_ /= g;
            d_ /= g;
        }
    }

    Fraction(const Fraction& f)
        : n_(f.get_num()), d_(f.get_denom()), reduce_(f.reduce_) {}

    // 値を返す(double型に変換)
    double value_dbl() const noexcept { return (double)n_ / d_; }

    // 分子, 分母のpair型を取得する
    pair<long long, long long> get_num_denom() const noexcept {
        return {n_, d_};
    }

    // 分子を取得する
    long long get_num() const noexcept { return n_; }

    // 分母を取得する
    long long get_denom() const noexcept { return d_; }

    // 比較演算子
    // @note
    // 分子・分母の掛け算が発生するため分子、分母がint型の範囲でないとオーバーフローの可能性あり
    friend constexpr bool operator<(const Fraction& lhs,
                                    const Fraction& rhs) noexcept {
        return lhs.n_ * rhs.d_ < rhs.n_ * lhs.d_;
    }

    friend bool operator==(const Fraction& lhs, const Fraction& rhs) {
        return lhs.n_ * rhs.d_ == rhs.n_ * lhs.d_;
    }

    friend bool operator!=(const Fraction& lhs, const Fraction& rhs) {
        return !(lhs == rhs);
    }

    // 四則演算子
    Fraction operator+() const { return *this; }

    Fraction operator-() const {
        auto [n, d] = get_num_denom();
        return Fraction(-n, d);
    }

    Fraction& operator+=(const Fraction& rhs) {
        auto [n, d] = rhs.get_num_denom();

        auto l = lcm(d, d_);

        n_ = n_ * (l / d_) + n * (l / d);
        d_ = l;

        if (reduce_) {
            auto g = gcd(abs(n_), d_);

            n_ /= g;
            d_ /= g;
        }

        return *this;
    }

    Fraction& operator-=(const Fraction& rhs) {
        *this += -rhs;
        return *this;
    }

    Fraction& operator*=(const Fraction& rhs) {
        auto [n, d] = rhs.get_num_denom();

        if (reduce_ && !rhs.reduce_) {
            auto g = gcd(abs(n), d);
            n /= g;
            d /= g;
        }

        n_ *= n;
        d_ *= d;

        if (d_ == 0) {
            n_ = 1;
        }

        return *this;
    }

    Fraction& operator/=(const Fraction& rhs) {
        auto [n, d] = rhs.get_num_denom();
        *this *= Fraction(d, n);

        return *this;
    }

    friend Fraction operator+(const Fraction& lhs, const Fraction& rhs) {
        return Fraction(lhs) += rhs;
    }

    friend Fraction operator-(const Fraction& lhs, const Fraction& rhs) {
        return Fraction(lhs) -= rhs;
    }

    friend Fraction operator*(const Fraction& lhs, const Fraction& rhs) {
        return Fraction(lhs) *= rhs;
    }

    friend Fraction operator/(const Fraction& lhs, const Fraction& rhs) {
        return Fraction(lhs) /= rhs;
    }

    friend ostream& operator<<(ostream& os, const Fraction& rhs) {
        auto [n, d] = rhs.get_num_denom();
        auto v = rhs.value_dbl();

        os << n << " / " << d << " = " << v;
        return os;
    }

   protected:
    long long n_;  // 分子
    long long d_;  // 分母
    bool reduce_;  // 通分フラグ
};

int main() {
    ll n;
    cin >> n;
    vector<ll> a(n, 0), b(n, 0);
    rep(i, n) cin >> a[i] >> b[i];

    vector<pair<Fraction, ll>> order;
    rep(i, n) { order.emplace_back(Fraction(a[i], a[i] + b[i], true), -i); }

    sort(order.rbegin(), order.rend());
    rep(i, n) { cout << -order[i].second + 1 << "\n"; }
    return 0;
}