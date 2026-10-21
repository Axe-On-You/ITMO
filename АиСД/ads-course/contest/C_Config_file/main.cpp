#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

map<string, vector<int> > a;
vector<vector<string> > b;

int main() {
  string s;
  b.push_back(vector<string>());
  while (cin >> s) {
    if (s == "{") {
      b.push_back(vector<string>());
    } else {
      if (s == "}") {
        int n = (int)b.back().size();
        for (int i = 0; i < n; i++) {
          a[b.back()[i]].pop_back();
        }
        b.pop_back();
      } else {
        int p = 0;
        for (int i = 0; i < (int)s.length(); i++) {
          if (s[i] == '=') {
            p = i;
            break;
          }
        }
        string x = "";
        string y = "";
        for (int i = 0; i < p; i++) {
          x += s[i];
        }
        for (int i = p + 1; i < (int)s.length(); i++) {
          y += s[i];
        }
        int v = 0;
        if (y[0] == '-' || (y[0] >= '0' && y[0] <= '9')) {
          int c = 1;
          int st = 0;
          if (y[0] == '-') {
            c = -1;
            st = 1;
          }
          int r = 0;
          for (int i = st; i < (int)y.length(); i++) {
            r = r * 10 + (y[i] - '0');
          }
          v = r * c;
        } else {
          if (a.find(y) == a.end()) {
            v = 0;
          } else {
            if (a[y].size() == 0) {
              v = 0;
            } else {
              v = a[y].back();
            }
          }
          cout << v << "\n";
        }
        a[x].push_back(v);
        b.back().push_back(x);
      }
    }
  }
  return 0;
}