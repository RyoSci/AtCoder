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
#define rep(i, n) for (int i = 0; i < n; i++)
#define rep_r(i, k, n) for (int i = k; i > n; i--)
#define rep_s(i, k, n) for (int i = k; i < n; i++)

int main() {
    int n, m;
    cin >> n >> m;
    set<int> a, b;
    rep(i, n) {
        int ai;
        cin >> ai;
        a.insert(ai);
    }
    rep(i, m) {
        int bi;
        cin >> bi;
        b.insert(bi);
    }
    vector<int> ans;
    for (auto i : a) {
        if (b.count(i)) continue;
        ans.push_back(i);
    }
    for (auto i : b) {
        if (a.count(i)) continue;
        ans.push_back(i);
    }
    sort(ans.begin(), ans.end());
    for (int a : ans) cout << a << " ";
    cout << endl;
    return 0;
}