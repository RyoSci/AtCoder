#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const long long INF = 1e18;

int n;
vector<vector<int>> d;
long long ans = 0;
vector<bool> used;

void dfs(int i, long long now = 0) {
    ans = max(ans, now);

    if (i == n) {
        return;
    }

    dfs(i + 1, now);

    for (int j = i + 1; j < n; j++) {
        if (used[j] || used[i]) {
            continue;
        }

        used[i] = true;
        used[j] = true;
        dfs(i + 1, now + d[i][j - i - 1]);
        used[i] = false;
        used[j] = false;
    }
}

int main() {
    cin >> n;
    d.resize(n - 1, vector<int>(n - 1));

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            cin >> d[i][j - i - 1];
        }
    }

    used.resize(n, false);
    dfs(0);

    cout << ans << endl;

    return 0;
}
