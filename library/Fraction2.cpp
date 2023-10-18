// https://atcoder.jp/contests/abc308/submissions/43095005
// line 1 "answer.cpp"
#if !__INCLUDE_LEVEL__
#include __FILE__
int main() {
    ll n;
    input(n);
    vector<pair<Frac, ll>> v;
    rep(i, n) {
        ll a, b;
        input(a, b);
        v.emplace_back(Frac(-a, a + b), i + 1);
    }
    sort(all(v));
    vl ans;
    rep(i, n) ans.push_back(v[i].second);
    print(ans);
}
#else
// line 2
// "/home/seekworser/.cpp_lib/competitive_library/competitive/std/std.hpp"
#include <bits/stdc++.h>
#ifndef LOCAL_TEST
#pragma GCC target("avx")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#endif  // LOCAL_TEST
using namespace std;
// shorten typenames
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vvi = vector<vi>;
using vvvi = vector<vvi>;
using vl = vector<ll>;
using vvl = vector<vl>;
using vvvl = vector<vvl>;
using vb = vector<bool>;
using vvb = vector<vb>;
using vvvb = vector<vvb>;
using vc = vector<char>;
using vvc = vector<vc>;
using vvvc = vector<vvc>;
using vd = vector<double>;
using vvd = vector<vd>;
using vvvd = vector<vvd>;
using vs = vector<string>;
using vvs = vector<vector<string>>;
using vvvs = vector<vector<vector<string>>>;
template <typename T>
vector<vector<T>> vv(int h, int w, T val = T()) {
    return vector(h, vector<T>(w, val));
}
template <typename T>
vector<vector<vector<T>>> vvv(int h1, int h2, int h3, T val = T()) {
    return vector(h1, vector(h2, vector<T>(h3, val)));
}
template <typename T>
vector<vector<vector<vector<T>>>> vvvv(int h1, int h2, int h3, int h4,
                                       T val = T()) {
    return vector(h1, vector(h2, vector(h3, vector<T>(h4, val))));
}
template <class T>
using priority_queue_min = priority_queue<T, vector<T>, greater<T>>;
// define CONSTANTS
constexpr double PI = 3.14159265358979323;
constexpr int INF = 100100111;
constexpr ll INFL = 3300300300300300491LL;
float EPS = 1e-8;
double EPSL = 1e-10;
template <typename T>
bool eq(const T x, const T y) {
    return x == y;
}
template <>
bool eq<double>(const double x, const double y) {
    return (abs(x - y) < EPSL * x || abs(x - y) < EPSL);
}
template <>
bool eq<float>(const float x, const float y) {
    return abs(x - y) < EPS * x;
}
template <typename T>
bool neq(const T x, const T y) {
    return !(eq<T>(x, y));
}
template <typename T>
bool ge(const T x, const T y) {
    return (eq<T>(x, y) || (x > y));
}
template <typename T>
bool le(const T x, const T y) {
    return (eq<T>(x, y) || (x < y));
}
template <typename T>
bool gt(const T x, const T y) {
    return !(le<T>(x, y));
}
template <typename T>
bool lt(const T x, const T y) {
    return !(ge<T>(x, y));
}
constexpr int MODINT998244353 = 998244353;
constexpr int MODINT1000000007 = 1000000007;
// fasten io
struct Nyan {
    Nyan() {
        cin.tie(nullptr);
        ios::sync_with_stdio(false);
        cout << fixed << setprecision(18);
    }
} nyan;
// define macros
#define all(a) (a).begin(), (a).end()
#define sz(x) ((ll)(x).size())
#define rep1(n) \
    for (ll dummy_iter = 0LL; dummy_iter < n; ++dummy_iter)  // 0,1,...,n-1
#define rep2(i, n)                                           \
    for (ll i = 0LL, i##_counter = 0LL; i##_counter < ll(n); \
         ++(i##_counter), (i) = i##_counter)  // i=0,1,...,n-1
#define rep3(i, s, t)                                            \
    for (ll i = ll(s), i##_counter = ll(s); i##_counter < ll(t); \
         ++(i##_counter), (i) = (i##_counter))  // i=s,s+1,...,t-1
#define rep4(i, s, t, step)                                            \
    for (ll i##_counter = step > 0 ? ll(s) : -ll(s),                   \
            i##_end = step > 0 ? ll(t) : -ll(t), i##_step = abs(step), \
            i = ll(s);                                                 \
         i##_counter<i##_end; i##_counter += i##_step, i = step> 0     \
             ? i##_counter                                             \
             : -i##_counter)  // i=s,s+step,...,<t
#define overload4(a, b, c, d, e, ...) e
#define rep(...) overload4(__VA_ARGS__, rep4, rep3, rep2, rep1)(__VA_ARGS__)
#define repe(a, v) for (auto& a : (v))  // iterate over all elements in v
#define smod(n, m) ((((n) % (m)) + (m)) % (m))
#define sdiv(n, m) (((n)-smod(n, m)) / (m))
#define uniq(a)                               \
    {                                         \
        sort(all(a));                         \
        (a).erase(unique(all(a)), (a).end()); \
    }
int Yes(bool b = true) {
    cout << (b ? "Yes\n" : "No\n");
    return 0;
};
int YES(bool b = true) {
    cout << (b ? "YES\n" : "NO\n");
    return 0;
};
int No(bool b = true) { return Yes(!b); };
int NO(bool b = true) { return YES(!b); };
template <typename T, size_t N>
T max(array<T, N> &a) {
    return *max_element(all(a));
};
template <typename T, size_t N>
T min(array<T, N> &a) {
    return *min_element(all(a));
};
template <typename T>
T max(vector<T> &a) {
    return *max_element(all(a));
};
template <typename T>
T min(vector<T> &a) {
    return *min_element(all(a));
};
template <typename T>
vector<T> vec_slice(const vector<T> &a, int l, int r) {
    vector<T> rev;
    rep(i, l, r) rev.push_back(a[i]);
    return rev;
};
template <typename T>
T sum(vector<T> &a, T zero = T(0)) {
    T rev = zero;
    rep(i, sz(a)) rev += a[i];
    return rev;
};
template <typename T>
bool in_range(const T &val, const T &s, const T &t) {
    return s <= val && val < t;
};

template <class T>
inline vector<T> &operator--(vector<T> &v) {
    repe(x, v)-- x;
    return v;
}
template <class T>
inline vector<T> &operator++(vector<T> &v) {
    repe(x, v)++ x;
    return v;
}

ll powm(ll a, ll n, ll mod = INFL) {
    ll res = 1;
    while (n > 0) {
        if (n & 1) res = (res * a) % mod;
        if (n > 1) a = (a * a) % mod;
        n >>= 1;
    }
    return res;
}
ll sqrtll(ll x) {
    assert(x >= 0);
    ll rev = sqrt(x);
    while (rev * rev > x) --rev;
    while ((rev + 1) * (rev + 1) <= x) ++rev;
    return rev;
}
template <class T>
inline bool chmax(T &M, const T &x) {
    if (M < x) {
        M = x;
        return true;
    }
    return false;
}
template <class T>
inline bool chmin(T &m, const T &x) {
    if (m > x) {
        m = x;
        return true;
    }
    return false;
}
int digit(ll x, int d = 10) {
    int rev = 0;
    while (x > 0) {
        rev++;
        x /= d;
    };
    return rev;
}
/**
 * @brief std.hpp
 * @docs docs/std/std.md
 */
// line 3
// "/home/seekworser/.cpp_lib/competitive_library/competitive/math/fraction.hpp"
struct Frac {
    ll num;
    ll den;
    Frac(ll _num, ll _den, bool reduce = true) : num(_num), den(_den) {
        if (reduce) (*this).reduce();
    }
    Frac(ll _num) : Frac(_num, 1) {}
    static ll redcue_limit;

    Frac inv() const { return Frac((*this).den, (*this).num); }
    Frac &operator+=(const Frac &x) {
        (*this).num = (*this).num * x.den + x.num * (*this).den;
        (*this).den = (*this).den * x.den;
        if ((*this).den > redcue_limit || (*this).num > redcue_limit)
            (*this).reduce();
        return (*this);
    }
    Frac &operator-=(const Frac &x) {
        (*this).num = (*this).num * x.den - x.num * (*this).den;
        (*this).den = (*this).den * x.den;
        if ((*this).den > redcue_limit || (*this).num > redcue_limit)
            (*this).reduce();
        return (*this);
    }
    Frac &operator*=(const Frac &x) {
        (*this).num = (*this).num * x.num;
        (*this).den = (*this).den * x.den;
        if ((*this).den > redcue_limit || (*this).num > redcue_limit)
            (*this).reduce();
        return (*this);
    }
    Frac &operator/=(const Frac &x) {
        (*this) *= x.inv();
        if ((*this).den > redcue_limit || (*this).num > redcue_limit)
            (*this).reduce();
        return (*this);
    }
    Frac operator+(const Frac &x) const { return (Frac(*this) += x); }
    Frac operator-(const Frac &x) const { return (Frac(*this) -= x); }
    Frac operator*(const Frac &x) const { return (Frac(*this) *= x); }
    Frac operator/(const Frac &x) const { return (Frac(*this) /= x); }

    Frac operator+() const { return *this; }
    Frac operator-() const {
        Frac x(-(*this).num, (*this).den);
        return x;
    }
    friend bool operator==(const Frac &lhs, const Frac &rhs) {
        return lhs.num * rhs.den == lhs.den * rhs.num;
    }
    friend bool operator!=(const Frac &lhs, const Frac &rhs) {
        return lhs.num * rhs.den != lhs.den * rhs.num;
    }
    friend bool operator>=(const Frac &lhs, const Frac &rhs) {
        return lhs.num * rhs.den >= lhs.den * rhs.num;
    }
    friend bool operator<=(const Frac &lhs, const Frac &rhs) {
        return lhs.num * rhs.den <= lhs.den * rhs.num;
    }
    friend bool operator>(const Frac &lhs, const Frac &rhs) {
        return lhs.num * rhs.den > lhs.den * rhs.num;
    }
    friend bool operator<(const Frac &lhs, const Frac &rhs) {
        return lhs.num * rhs.den < lhs.den * rhs.num;
    }

    double val() const { return (double)((*this).num) / (double)((*this).den); }
    friend ostream &operator<<(ostream &os, const Frac &x) {
        os << x.val();
        return os;
    }
    void reduce() {
        assert((*this).den != 0 || (*this).num != 0);
        if ((*this).den == 0) {
            (*this).num = 1;
            return;
        }
        if ((*this).num == 0) {
            (*this).den = 1;
            return;
        }
        ll g = gcd((*this).num, (*this).den);
        (*this).num /= g;
        (*this).den /= g;
        if ((*this).den < 0) {
            (*this).num *= -1;
            (*this).den *= -1;
        }
        return;
    }
};
ll Frac::redcue_limit = 1000000000;
Frac pow(const Frac &a, ll n) {
    Frac res(1);
    Frac cur(a);
    while (n > 0) {
        if (n & 1) res *= cur;
        cur *= cur;
        n >>= 1;
    }
    return res;
}
Frac abs(const Frac &f) {
    Frac rev(f);
    if (rev.den * rev.num < 0) return -rev;
    return rev;
}
/**
 * @brief fraction.hpp
 * @docs docs/math/fraction.md
 */
// line 3 "/home/seekworser/.cpp_lib/competitive_library/competitive/std/io.hpp"
// overload operators (prototypes)
template <class T, class U>
inline istream &operator>>(istream &is, pair<T, U> &p);
template <class T>
inline istream &operator>>(istream &is, vector<T> &v);
template <class T, class U>
inline ostream &operator<<(ostream &os, const pair<T, U> &p);
template <class T>
inline ostream &operator<<(ostream &os, const vector<T> &v);
template <typename T, typename S>
ostream &operator<<(ostream &os, const map<T, S> &mp);
template <typename T>
ostream &operator<<(ostream &os, const set<T> &st);
template <typename T>
ostream &operator<<(ostream &os, const multiset<T> &st);
template <typename T>
ostream &operator<<(ostream &os, const unordered_set<T> &st);
template <typename T>
ostream &operator<<(ostream &os, queue<T> q);
template <typename T>
ostream &operator<<(ostream &os, deque<T> q);
template <typename T>
ostream &operator<<(ostream &os, stack<T> st);
template <class T, class Container, class Compare>
ostream &operator<<(ostream &os, priority_queue<T, Container, Compare> pq);

// overload operators
template <class T, class U>
inline istream &operator>>(istream &is, pair<T, U> &p) {
    is >> p.first >> p.second;
    return is;
}
template <class T>
inline istream &operator>>(istream &is, vector<T> &v) {
    repe(x, v) is >> x;
    return is;
}
template <class T, class U>
inline ostream &operator<<(ostream &os, const pair<T, U> &p) {
    os << p.first << " " << p.second;
    return os;
}
template <class T>
inline ostream &operator<<(ostream &os, const vector<T> &v) {
    rep(i, sz(v)) {
        os << v.at(i);
        if (i != sz(v) - 1) os << " ";
    }
    return os;
}
template <typename T, typename S>
ostream &operator<<(ostream &os, const map<T, S> &mp) {
    for (auto &[key, val] : mp) {
        os << key << ":" << val << " ";
    }
    return os;
}
template <typename T>
ostream &operator<<(ostream &os, const set<T> &st) {
    auto itr = st.begin();
    for (int i = 0; i < (int)st.size(); i++) {
        os << *itr << (i + 1 != (int)st.size() ? " " : "");
        itr++;
    }
    return os;
}
template <typename T>
ostream &operator<<(ostream &os, const multiset<T> &st) {
    auto itr = st.begin();
    for (int i = 0; i < (int)st.size(); i++) {
        os << *itr << (i + 1 != (int)st.size() ? " " : "");
        itr++;
    }
    return os;
}
template <typename T>
ostream &operator<<(ostream &os, const unordered_set<T> &st) {
    ll cnt = 0;
    for (auto &e : st) {
        os << e << (++cnt != (int)st.size() ? " " : "");
    }
    return os;
}
template <typename T>
ostream &operator<<(ostream &os, queue<T> q) {
    while (q.size()) {
        os << q.front() << " ";
        q.pop();
    }
    return os;
}
template <typename T>
ostream &operator<<(ostream &os, deque<T> q) {
    while (q.size()) {
        os << q.front() << " ";
        q.pop_front();
    }
    return os;
}
template <typename T>
ostream &operator<<(ostream &os, stack<T> st) {
    while (st.size()) {
        os << st.top() << " ";
        st.pop();
    }
    return os;
}
template <class T, class Container, class Compare>
ostream &operator<<(ostream &os, priority_queue<T, Container, Compare> pq) {
    while (pq.size()) {
        os << pq.top() << " ";
        pq.pop();
    }
    return os;
}

template <typename T>
int print_sep_end(string sep, string end, const T &val) {
    (void)sep;
    cout << val << end;
    return 0;
};
template <typename T1, typename... T2>
int print_sep_end(string sep, string end, const T1 &val, const T2 &...remain) {
    cout << val << sep;
    print_sep_end(sep, end, remain...);
    return 0;
};
template <typename... T>
int print(const T &...args) {
    print_sep_end(" ", "\n", args...);
    return 0;
};
template <typename... T>
void flush() {
    cout << flush;
};
template <typename... T>
int print_and_flush(const T &...args) {
    print(args...);
    flush();
    return 0;
};
#define debug(...) debug_func(0, #__VA_ARGS__, __VA_ARGS__)  // debug print
template <typename T>
void input(T &a) {
    cin >> a;
};
template <typename T1, typename... T2>
void input(T1 &a, T2 &...b) {
    cin >> a;
    input(b...);
};
#ifdef LOCAL_TEST
template <typename T>
void debug_func(int i, const T name) {
    (void)i;
    (void)name;
    cerr << endl;
}
template <typename T1, typename T2, typename... T3>
void debug_func(int i, const T1 &name, const T2 &a, const T3 &...b) {
    int scope = 0;
    for (; (scope != 0 || name[i] != ',') && name[i] != '\0'; i++) {
        cerr << name[i];
        if (name[i] == '(' || name[i] == '{') scope++;
        if (name[i] == ')' || name[i] == '}') scope--;
    }
    cerr << ":" << a << " ";
    debug_func(i + 1, name, b...);
}
template <typename T1, typename T2, typename... T3>
void debug_func(int i, const T1 &name, T2 &a, T3 &...b) {
    int scope = 0;
    for (; (scope != 0 || name[i] != ',') && name[i] != '\0'; i++) {
        cerr << name[i];
        if (name[i] == '(' || name[i] == '{') scope++;
        if (name[i] == ')' || name[i] == '}') scope--;
    }
    cerr << ":" << a << " ";
    debug_func(i + 1, name, b...);
}
#endif
#ifndef LOCAL_TEST
template <typename... T>
void debug_func(T &...) {}
template <typename... T>
void debug_func(const T &...) {}
#endif
/**
 * @brief io.hpp
 * @docs docs/std/io.md
 */
// line 21 "answer.cpp"
#endif
