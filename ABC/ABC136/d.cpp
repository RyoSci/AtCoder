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
    string s;
    cin >> s;
    Int n = s.length();
    vector<Int> ans(n);
    vector<tuple<char, Int, Int>> zaatsu;
    char now = 'R';
    Int cnt = 0;
    rep(i, n) {
        if (s[i] == now) {
            cnt++;
        } else {
            zaatsu.push_back(make_tuple(now, cnt, i));
            now = s[i];
            cnt = 1;
        }
    }
    zaatsu.push_back(make_tuple(now, cnt, n - 1));

    rep(i, zaatsu.size()) {
        tuple<char, Int, Int> x = zaatsu[i];
        if (get<0>(x) == 'R') {
            ans[get<2>(x)] += get<1>(x) / 2;
            ans[get<2>(x) - 1] += get<1>(x) / 2 + get<1>(x) % 2;
        } else {
            Int tmp = get<2>(zaatsu[i - 1]);
            ans[tmp] += get<1>(x) / 2 + get<1>(x) % 2;
            ans[tmp - 1] += get<1>(x) / 2;
        }
    }

    for (Int a : ans) cout << a << " ";
    cout << endl;
    return 0;
}