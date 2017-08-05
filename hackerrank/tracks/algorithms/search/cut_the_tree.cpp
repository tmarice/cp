#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Node {
    public:
        int data;
        int cumsum;
        vector<int> links;
        Node(int data): data(data), cumsum(data) {}
};


vector<Node*> nodes;

int fix_cumsums(Node *node, Node *parent) {
    int cumsum = 0;

    for (int i = 0; i < node->links.size(); ++i) 
        if (nodes[node->links[i]] != parent)
            cumsum += fix_cumsums(nodes[node->links[i]], node);
    
    node->cumsum += cumsum;

    return node->cumsum;
}


int main() {
    int n;
    cin >> n;

    int d;
    for (int i = 0; i < n; ++i) {
        cin >> d;
        nodes.push_back(new Node(d));
    }

    int a, b;
    for (int i = 0; i < n-1; ++i) {
        cin >> a >> b;
        --a; --b;

        nodes[a]->links.push_back(b);
        nodes[b]->links.push_back(a);
    }

    fix_cumsums(nodes[0], NULL);

    int out = 1000000000;
    for (int i = 1; i < n; ++i)
        out = min(out, abs(nodes[0]->cumsum - 2 * nodes[i]->cumsum));

    cout << out << endl;

    return 0;
}

