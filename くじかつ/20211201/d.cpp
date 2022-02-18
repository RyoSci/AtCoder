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
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (Int i = 0; i < n; i++)
#define rep_r(i, k, n) for (Int i = k; i > n; i--)
#define rep_s(i, k, n) for (Int i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)

int main() {
    Int n;
    cin >> n;
    set<Int> keys;
    map<Int, Int> d;
    rep(i, n) {
        Int a, b;
        cin >> a >> b;
        d[a]++;
        d[a + b]--;
        keys.insert(a);
        keys.insert(a + b);
    }
    vector<Int> keys_vec;
    for (Int a : keys) {
        keys_vec.push_back(a);
    }

    sort(keys_vec.begin(), keys_vec.end());
    Int m = keys_vec.size();
    vector<Int> ans(n + 1);
    rep(i, m - 1) {
        d[keys_vec[i + 1]] += d[keys_vec[i]];
        ans[d[keys_vec[i]]] += (keys_vec[i + 1] - keys_vec[i]);
    }
    rep_s(i, 1, n + 1) { cout << ans[i] << "\n"; }

    return 0;
}