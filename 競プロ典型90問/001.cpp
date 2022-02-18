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
#define rep_e(c, s) for (auto c : s)

vector<int> A;
int K;

bool f(int m) {
    int cnt = 0;
    int now = 0;
    rep_e(e, A) {
        if (e - now >= m) {
            cnt++;
            now = e;
        }
    }
    return cnt >= K + 1;
}

int main() {
    int N, L;
    cin >> N >> L;
    cin >> K;
    A.resize(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    A.push_back(L);
    int l = 0;
    int r = L;
    while (l + 1 < r) {
        int m = (l + r) / 2;
        if (f(m))
            l = m;
        else
            r = m;
    }

    cout << l << "\n";
    return 0;
}