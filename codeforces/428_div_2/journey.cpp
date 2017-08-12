
#include <iostream>
#include <iomanip>
#include <unordered_map>
#include <vector>
using namespace std;


unordered_map<int, vector<int>> graph;


double journey(double prob, int length, int node, int parent) {
    vector<int> children;
    for (auto child: graph[node]) {
        if (child != parent)
            children.push_back(child);
    }

    int n_children = children.size();

    if (n_children == 0)
        return prob * length;
    else {
        double new_prob = prob / n_children;
        double ret = 0.0;

        for (auto child: children)
            ret += journey(new_prob, length + 1, child, node);

        return ret;
    }
}



int main() {
    int n, u, v;

    cin >> n;

    for (int i = 0; i < n - 1; ++i) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    cout << fixed << setprecision(6) << journey(1.0, 0, 1, -1) << endl;

    return 0;
}
