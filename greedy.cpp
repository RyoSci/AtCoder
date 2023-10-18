#include <bits/stdc++.h>

#pragma GCC optimize(3, "Ofast", "inline")
#define ull unsigned long long
#define int long long
#define ll long long
#define ld long double
#define pii pair<ll, ll>
#define endl '\n'
#define x first
#define y second

using namespace std;

const ld eps = 1e-6;
const int N = 100010, M = 100010, inf = 1e9, mod = 998244353;

int n, m, k;
int a[N], cnt[N], f[N];
vector<int> g[N];
map<pii, int> ma;

bool dfs(int u, int fa, int goal) {
    if (u == goal) return true;
    for (int v : g[u]) {
        if (v == fa) continue;
        if (dfs(v, u, goal)) {
            cnt[ma[{u, v}]]++;
            return true;
        }
    }
    return false;
}

void solve() {
    cin >> n >> m >> k;
    k = abs(k);
    for (int i = 1; i <= m; i++) {
        cin >> a[i];
    }
    for (int i = 1; i < n; i++) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
        ma[{a, b}] = ma[{b, a}] = i;
    }

    for (int i = 2; i <= m; i++) {
        dfs(a[i - 1], 0, a[i]);
    }

    int sum = 0;
    for (int i = 1; i < n; i++) {
        sum += cnt[i];
    }

    f[sum] = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= sum; j++) {
            if (j + 2 * cnt[i] > sum) break;
            f[j] += f[j + 2 * cnt[i]];
            f[j] %= mod;
        }
    }
    cout << f[k] << endl;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t = 1;
    // cin>>t;
    while (t--) solve();

    return 0;
}