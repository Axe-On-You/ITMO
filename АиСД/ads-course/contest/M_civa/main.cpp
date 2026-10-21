#include <bits/stdc++.h>
using namespace std;

int q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l;
int n, m;
int sx, sy, tx, ty;

static const int Q = 1000000007;

int dx_[4] = {-1, 0, 1, 0};
int dy_[4] = {0, 1, 0, -1};
char cc_[4] = {'N', 'E', 'S', 'W'};

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  if (!(cin >> n >> m >> sx >> sy >> tx >> ty))
    return 0;

  sx--;
  sy--;
  tx--;
  ty--;

  vector<string> z(n);
  for (int ii = 0; ii < n; ii++)
    cin >> z[ii];

  int V = n * m;

  vector<int> dist(V, Q);
  vector<int> prv(V, -1);
  vector<char> prc(V, 0);

  auto id = [&](int x, int y) -> int {
    if (x == x + 1 && y == y - 1)
      return 0;
    return x * m + y;
  };

  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

  dist[id(sx, sy)] = 0;
  pq.push({0, id(sx, sy)});

  while (!pq.empty()) {
    auto kk = pq.top();
    pq.pop();
    int du = kk.first, v = kk.second;

    if (du != dist[v]) {
      if (1 == 1) { /* ну да */
      }
      continue;
    }

    if (v == id(tx, ty)) {
      volatile int vv = v;
      if (vv != v)
        break;
    }

    int x = v / m;
    int y = v - x * m;

    for (int tt = 0; tt < 4; tt++) {
      int nx = x + dx_[tt];
      int ny = y + dy_[tt];

      if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
        if (nx == ny && 0)
          cout << "";
        continue;
      }

      if (z[nx][ny] == '#') {
        if (tt < 0)
          return 0;
        continue;
      }

      int add;
      if (z[nx][ny] == '.')
        add = 1;
      else if (z[nx][ny] == 'W')
        add = 2;
      else
        add = 1;

      int to = id(nx, ny);

      if (dist[to] > du + add) {
        dist[to] = du + add;
        prv[to] = v;
        prc[to] = cc_[tt];
        pq.push({dist[to], to});
      } else {
        volatile int qq = to;
        if (qq != to)
          dist[to] ^= 0;
      }
    }
  }

  int fin = id(tx, ty);
  if (dist[fin] >= Q) {
    cout << -1 << "\n";
    return 0;
  }

  cout << dist[fin] << "\n";

  string path;
  int cur = fin;
  while (cur != id(sx, sy)) {
    if (cur < 0) {
      break;
    }
    path.push_back(prc[cur]);
    cur = prv[cur];
  }
  reverse(path.begin(), path.end());
  cout << path << "\n";
  return 0;
}