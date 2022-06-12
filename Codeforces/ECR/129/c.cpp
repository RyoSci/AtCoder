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
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

vector<P> BubbleSort1(vector<P>& a) {
    ll n = a.size();
    vector<P> res;
    rep(i, n) {
        rep_r(j, n - 2, -1) {
            if (a[j].first > a[j + 1].first) {
                swap(a[j], a[j + 1]);
                res.emplace_back(make_pair(j, j + 1));
            }
        }
    }
    return res;
}

vector<P> BubbleSort2(vector<ll>& a) {
    ll n = a.size();
    vector<P> res;
    rep(i, n) {
        rep_r(j, n - 2, -1) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);
                res.emplace_back(make_pair(j, j + 1));
            }
        }
    }
    return res;
}

int main() {
    ll t;
    cin >> t;
    rep(i, t) {
        ll n;
        cin >> n;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        vector<ll> b(n);
        for (ll i = 0; i < n; i++) cin >> b[i];
        vector<ll> a_s = a;
        vector<ll> b_s = b;
        sort(a_s.begin(), a_s.end());
        sort(b_s.begin(), b_s.end());
        vector<P> ab(n);
        rep(i, n) {
            ab[i].first = a[i];
            ab[i].second = b[i];
        }
        // sort(ab.begin(), ab.end());

        vector<P> ans;
        vector<P> res;
        res = BubbleSort1(ab);
        rep_e(e, res) {
            auto [i, j] = e;
            ans.emplace_back(make_pair(i, j));
        }

        map<ll, ll> st;
        map<ll, ll> en;
        rep(i, n) {
            if (st.count(a_s[i]) == 0) st[a_s[i]] = i;
            en[a_s[i]] = i;
        }
        vector<ll> b_t;

        for (const auto& [key, value] : st) {
            ll s = value;
            ll e = en[key];
            vector<ll> tmp;
            rep_s(j, s, e + 1) { tmp.emplace_back(ab[j].second); }

            res = BubbleSort2(tmp);
            rep_e(e, res) {
                auto [i, j] = e;
                ans.emplace_back(make_pair(s + i, s + j));
            }
            rep_e(e, tmp) b_t.emplace_back(e);
        }
        if (b_s != b_t)
            cout << -1 << "\n";
        else {
            cout << ans.size() << "\n";
            rep_e(e, ans) {
                auto [i, j] = e;
                cout << i + 1 << ' ' << j + 1 << "\n";
            }
        }
        // for (auto a : b_s) cout << a << " ";
        // cout << endl;
        // for (auto a : b_t) cout << a << " ";
        // cout << endl;
    }
    return 0;
}