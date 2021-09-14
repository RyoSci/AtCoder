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

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

Int cnt, res;
string str;
int main()
{
    int n;
    cin >> str;
    if (str.at(0) == str.at(1) && str.at(1) == str.at(2))
        cout << "Yes" << endl;
    else if (str.at(1) == str.at(2) && str.at(2) == str.at(3))
        cout << "Yes" << endl;
    else
        cout << "No" << endl;

    return 0;
}