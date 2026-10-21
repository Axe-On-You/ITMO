#include <iostream>
#include <map>

using namespace std;

long long q, w, e, r, t, y, u, i, o, p, s, d, f, g, k, l;
long long a[600005];
long long m[200005], n[200005];
int x[200005], h;
map<long long, int> z;
long long r1[100005], r2[100005];

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  if (!(cin >> q >> w))
    return 0;

  h = 200000;
  i = 1;
  while (i < h + 1) {
    x[i] = i;
    i = i + 1;
  }

  t = 1;
  m[x[h]] = 1;
  n[x[h]] = q;
  z[1] = x[h];

  y = 262144;
  a[y + x[h]] = q;
  u = (y + x[h]) / 2;
  while (u > 0) {
    a[u] = (a[u * 2] > a[u * 2 + 1] ? a[u * 2] : a[u * 2 + 1]);
    u = u / 2;
  }
  h = h - 1;

  t = 1;
  while (t < w + 1) {
    cin >> k;
    if (k > 0) {
      if (a[1] < k) {
        cout << "-1\n";
        r1[t] = 0;
        r2[t] = 0;
      } else {
        o = 1;
        while (o < y) {
          if (a[o * 2] >= k)
            o = o * 2;
          else
            o = o * 2 + 1;
        }
        int id = o - y;
        long long cur_p = m[id];
        long long cur_s = n[id];
        cout << cur_p << "\n";
        r1[t] = cur_p;
        r2[t] = k;

        z.erase(cur_p);
        if (cur_s == k) {
          a[o] = 0;
          h = h + 1;
          x[h] = id;
        } else {
          m[id] = cur_p + k;
          n[id] = cur_s - k;
          a[o] = n[id];
          z[m[id]] = id;
        }
        u = o / 2;
        while (u > 0) {
          a[u] = (a[u * 2] > a[u * 2 + 1] ? a[u * 2] : a[u * 2 + 1]);
          u = u / 2;
        }
      }
    } else {
      int target = -k;
      if (r2[target] > 0) {
        long long fr_p = r1[target];
        long long fr_s = r2[target];
        auto it = z.lower_bound(fr_p);
        int id_r = -1, id_l = -1;
        if (it != z.end() && it->first == fr_p + fr_s)
          id_r = it->second;
        if (it != z.begin()) {
          auto it_l = it;
          it_l--;
          if (m[it_l->second] + n[it_l->second] == fr_p)
            id_l = it_l->second;
        }

        if (id_l != -1 && id_r != -1) {
          z.erase(m[id_l]);
          z.erase(m[id_r]);
          a[y + id_r] = 0;
          u = (y + id_r) / 2;
          while (u > 0) {
            a[u] = (a[u * 2] > a[u * 2 + 1] ? a[u * 2] : a[u * 2 + 1]);
            u = u / 2;
          }
          h = h + 1;
          x[h] = id_r;
          n[id_l] += fr_s + n[id_r];
          a[y + id_l] = n[id_l];
          u = (y + id_l) / 2;
          while (u > 0) {
            a[u] = (a[u * 2] > a[u * 2 + 1] ? a[u * 2] : a[u * 2 + 1]);
            u = u / 2;
          }
          z[m[id_l]] = id_l;
        } else if (id_l != -1) {
          z.erase(m[id_l]);
          n[id_l] += fr_s;
          a[y + id_l] = n[id_l];
          u = (y + id_l) / 2;
          while (u > 0) {
            a[u] = (a[u * 2] > a[u * 2 + 1] ? a[u * 2] : a[u * 2 + 1]);
            u = u / 2;
          }
          z[m[id_l]] = id_l;
        } else if (id_r != -1) {
          z.erase(m[id_r]);
          m[id_r] = fr_p;
          n[id_r] += fr_s;
          a[y + id_r] = n[id_r];
          u = (y + id_r) / 2;
          while (u > 0) {
            a[u] = (a[u * 2] > a[u * 2 + 1] ? a[u * 2] : a[u * 2 + 1]);
            u = u / 2;
          }
          z[m[id_r]] = id_r;
        } else {
          int id = x[h];
          h = h - 1;
          m[id] = fr_p;
          n[id] = fr_s;
          a[y + id] = n[id];
          u = (y + id) / 2;
          while (u > 0) {
            a[u] = (a[u * 2] > a[u * 2 + 1] ? a[u * 2] : a[u * 2 + 1]);
            u = u / 2;
          }
          z[fr_p] = id;
        }
      }
    }
    t = t + 1;
  }
  return 0;
}