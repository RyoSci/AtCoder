// #define _GLIBCXX_DEBUG
#include <algorithm>
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
using lli = long long;
#define MOD 1000000007
#define INF (1L << 30)
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
    ll t;
    cin >> t;
    rep(_, t) {
        string s;
        cin >> s;
        ll l = 0, r = 0, ql = 0, qr = 0;
        ll n = s.size();
        rep(i, n) {
            if (s[i] == '(')
                l++;
            else if (s[i] == ')')
                r++;
        }
        if (l < r) {
            ql += r - l;
        } else if (l > r) {
            qr += l - r;
        }
        ll rest = n - l - r - ql - qr;
        ql += rest / 2;
        qr += rest / 2;

        if (ql == 0 or qr == 0)
            cout << "YES"
                 << "\n";
        else {
            ll cnt = 0;
            ll max_l;
            rep(i, n) {
                if (s[i] == '?') {
                    max_l = i;
                    cnt++;
                    s[i] = '(';
                }
                if (cnt == ql) break;
            }
            ll min_r = INF;
            rep_s(i, max_l + 1, n) {
                if (s[i] == '?') {
                    min_r = min(min_r, i);
                    s[i] = ')';
                }
            }
            ll tmp = s[max_l];
            s[max_l] = s[min_r];
            s[min_r] = tmp;

            stack<ll> st;
            rep(i, n) {
                if (s[i] == '(') {
                    st.emplace(s[i]);
                } else {
                    if (!st.empty() and st.top() == '(')
                        st.pop();
                    else
                        st.emplace(s[i]);
                }
            }
            if (st.empty())
                cout << "NO"
                     << "\n";
            else
                cout << "YES"
                     << "\n";
        }
    }
    return 0;
}