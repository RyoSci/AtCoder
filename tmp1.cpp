#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

const long long INF = 1e18;

int main() {
    int n;
    cin >> n;
    int a, b;
    cin >> a >> b;

    unordered_map<pair<int, int>, int> d;

    for (int i = 0; i < n; i++) {
        int p, q, r, s;
        cin >> p >> q >> r >> s;

        for (int x = p; x <= r; x++) {
            for (int y = q; y <= s; y++) {
                d[{x, y}]++;
            }
        }
    }

    int mx = 0;
    int area = 0;
    for (const auto entry : d) {
        mx = max(mx, entry.second);
    }

    for (const auto& entry : d) {
        if (entry.second == mx) {
            area++;
        }
    }

    cout << mx << endl;
    cout << area << endl;

    return 0;
}
