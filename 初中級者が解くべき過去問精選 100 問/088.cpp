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
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)
#define _GLIBCXX_DEBUG

int main() {
    ll n;
    cin >> n;
    stack<P> st;
    rep(i, n) {
        ll j;
        cin >> j;
        if (i % 2 == 0) {
            if (st.empty()) {
                st.push(make_pair(j, 1));
                continue;
            }
            ll id, cnt;
            tie(id, cnt) = st.top();
            st.pop();
            if (id == j) {
                st.push(make_pair(id, cnt + 1));
            } else {
                st.push(make_pair(id, cnt));
                st.push(make_pair(j, 1));
            }
        } else {
            ll id, cnt;
            tie(id, cnt) = st.top();
            st.pop();
            if (id != j) {
                ll id2, cnt2;
                cnt2 = 0;
                if (!st.empty()) {
                    tie(id2, cnt2) = st.top();
                    st.pop();
                }
                st.push(make_pair(j, cnt + cnt2 + 1));
            } else {
                st.push(make_pair(j, cnt + 1));
            }
        }
    }
    ll ans = 0;
    while (!st.empty()) {
        ll id, cnt;
        tie(id, cnt) = st.top();
        st.pop();
        if (id == 0) ans += cnt;
    }
    cout << ans << "\n";
    return 0;
}