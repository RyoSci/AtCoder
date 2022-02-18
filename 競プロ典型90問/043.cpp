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

int h, w, rs, cs, rt, ct;
int tmp;

string str;

int main()
{
    cin >> h >> w;
    cin >> rs >> cs;
    cin >> rt >> ct;

    rs--;
    cs--;
    rt--;
    ct--;

    // vector<vector<string> > s(h, vector<string>(w));
    // vector<vector<Int> > res(h, vector<Int>(w));
    string s[h][w];
    int res[h][w];

    for (int i = 0; i < h; i++)
    {
        string str;
        cin >> str;
        for (int j = 0; j < w; j++)
        {
            s[i][j] = str[j];
            res[i][j] = 10000000;
        }
    }

    res[rs][cs] = 0;

    queue<int> q;

    for (int i = 0; i < 4; i++)
    {
        q.push(rs);
        q.push(cs);
        q.push(0);
        q.push(i);
    }

    int proceed[4][2] = {
        {-1, 0},
        {1, 0},
        {0, 1},
        {0, -1}};

    while (!q.empty())
    {
        int tmp[4];
        for (int i = 0; i < 4; i++)
        {
            tmp[i] = q.front();
            q.pop();
        }
        int x = tmp[0];
        int y = tmp[1];
        int cnt = tmp[2];
        int dir = tmp[3];

        // cout << x << " " << y << " " << cnt << " " << dir << endl;
        for (int i = 0; i < 4; i++)
        {
            // cout << x + proceed[i][0] << " " << y + proceed[i][1] << endl;
            // cout << proceed[i][0] << " " << proceed[i][1] << endl;
            if ((0 <= x + proceed[i][0]) && (x + proceed[i][0] < h) && (0 <= y + proceed[i][1]) && (y + proceed[i][1] < w) && (s[x + proceed[i][0]][y + proceed[i][1]] == "."))
            {
                int is_not_dir = 0;
                if (i != dir)
                {
                    is_not_dir++;
                }
                // cout << x << " " << y << " " << is_not_dir << endl;
                if (res[x + proceed[i][0]][y + proceed[i][1]] >= cnt + is_not_dir)
                {
                    res[x + proceed[i][0]][y + proceed[i][1]] = cnt + is_not_dir;
                    q.push(x + proceed[i][0]);
                    q.push(y + proceed[i][1]);
                    q.push(cnt + is_not_dir);
                    q.push(i);
                }
            }
        }
    }

    cout << res[rt][ct] << endl;

    return 0;
}