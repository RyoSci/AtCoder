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

int main() {
    ll t;
    cin >> t;
    rep(_, t) {
        ll n;
        cin >> n;
        string s;
        cin >> s;

        deque<char> dq;
        rep(i, n) { dq.emplace_back(s[i]); }

        while (dq.size() > 1) {
            char l = dq.front();
            char r = dq.back();
            dq.pop_front();
            dq.pop_back();
            if (l == r) {
                dq.emplace_front(l);
                dq.emplace_back(r);
                break;
            }
        }

        cout << dq.size() << "\n";
    }
    return 0;
}