#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <stack>
using namespace std;
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;

vector<Int> n(4);
vector<Int> m{1, 4, 7, 9};
string ans;
int main()
{
    for (int i = 0; i < 4; i++)
    {
        cin >> n[i];
    }
    sort(n.begin(), n.end());
    ans = "YES";
    for (int i = 0; i < 4; i++)
    {
        if (n[i] != m[i])
        {
            ans = "NO";
            break;
        }
    }
    cout << ans << endl;
    return 0;
}