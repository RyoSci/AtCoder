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



int main()
{
    ll t;
    cin >> t;
    rep(_,t){
        ll n;
        cin >> n;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        vector<ll> b(n);
        for (ll i = 0; i < n; i++) cin >> b[i];
        
        map<ll, vector<ll>> da,db;
        priority_queue<T> q;
        vector<ll> seen_a(n) ,seen_b;

        rep(i, n) { 
            da[a[i]].emplace_back(i);
            q.emplace(T{a[i], 0, i});
        }

        rep(i, n){
            if (da[b[i]].size()>0) {
                da[b[i]]
            }
        }
    }
    return 0;
}