/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {

        return build(grid, 0, 0, grid.size());

    }

    Node* build(vector<vector<int>>& grid, int row, int col, int len) {
        if (checkUniformity(grid, row, col, len)) {
            return new Node(grid[row][col], true); 
        }
        
        int half = len / 2; 

        Node *tl = build(grid, row, col, half);
        Node *tr = build(grid, row, col + half, half);
        Node *bl = build(grid, row + half, col, half);
        Node *br = build(grid, row + half, col + half, half);

        return new Node(true, false, tl, tr, bl, br);
    }

    bool checkUniformity(vector<vector<int>>& grid, int row, int col, int len) {
        int num = grid[row][col];
        for (int i = row; i < row + len; i++) {
            for (int j = col; j < col + len; j++) {
                if (grid[i][j] != num) 
                    return false; 
            }
        }
        return true; 
    }


};