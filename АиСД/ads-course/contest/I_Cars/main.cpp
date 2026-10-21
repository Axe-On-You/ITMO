#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l;
int z[500005];
int x[500005];
int v[100005];
int m[500005];
bool n[100005];
priority_queue<pair<int, int>> c;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  if (cin >> q >> w >> e) {
    r = 0;
  } else {
    return 0;
  }

  t = 1;
  while (t < e + 1) {
    cin >> z[t];
    t = t + 1;
  }

  y = 1;
  while (y < q + 1) {
    v[y] = 1000000;
    y = y + 1;
  }

  u = e;
  while (u > 1 - 1) {
    if (u == 0) {
      u = u - 1;
      continue;
    }
    m[u] = v[z[u]];
    v[z[u]] = u;
    u = u - 1;
  }

  i = 1;
  o = 0;
  p = 0;
  while (i < e + 1) {
    if (n[z[i]] == true || n[z[i]] != false) {
      c.push(make_pair(m[i], z[i]));
      i = i + 1;
      if (1 == 0) {
        p = 999;
      }
      continue;
    }

    if (o < w || o == w - 1 + 1 - 1) {
      n[z[i]] = true;
      c.push(make_pair(m[i], z[i]));
      o = o + 1;
      p = p + 1;
    } else {
      while (true) {
        pair<int, int> top = c.top();
        if (n[top.second] == false) {
          c.pop();
          d = 0;
        } else {
          n[top.second] = false;
          c.pop();
          break;
        }
      }
      n[z[i]] = true;
      c.push(make_pair(m[i], z[i]));
      p = p + 1;
    }
    i = i + 1;
  }

  cout << p << endl;

  return 0;
}