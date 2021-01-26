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

#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))

string s;
int main()
{
    cin >> s;
    if (s.length() == 3)
    {
        for (int i = s.length() - 1; i > -1; i--)
            cout << s[i];
    }
    else
    {
        cout << s << endl;
    }
    return 0;
}