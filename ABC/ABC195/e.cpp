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

int main() {
    ll n;
    cin >> n;
    string s;
    cin >> s;
    string x;
    cin >> x;

    // map<P, bool> memo;

    auto f = [&](auto f, ll i, ll mask) {
        if (i == -1) {
            if (mask & 1)
                return true;
            else
                return false;
        }

        // if (memo.count(P(i, mask))) return memo[P(i, mask)];

        ll nmask = 0;
        vector<ll> a = {0, s[i] - '0'};

        if (i == 0 or x[i - 1] == x[i]) {
            rep(j, 7) {
                rep(k, 2) {
                    ll tmp = 10 * j + a[k];
                    tmp %= 7;
                    if (mask >> tmp & 1) nmask |= 1 << j;
                }
            }
            return f(f, i - 1, nmask);
            // return memo[P(i, mask)] = f(f, i - 1, nmask);
        } else {
            // mask ^= (1 << 7) - 1;
            rep(j, 7) {
                rep(k, 2) {
                    ll tmp = 10 * j + a[k];
                    tmp %= 7;
                    if ((mask >> tmp) & 1) nmask |= (1 << j);
                }
            }
            nmask ^= (1 << 7) - 1;
            return !f(f, i - 1, nmask);
            // return memo[P(i, mask)] = !f(f, i - 1, nmask);
        }
    };

    if (x[n - 1] == 'A') {
        cout << (f(f, n - 1, (1 << 7) - 2) ? "Aoki" : "Takahashi") << "\n";
    } else {
        cout << (f(f, n - 1, 1) ? "Takahashi" : "Aoki") << "\n";
    }
    return 0;
}