class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (dfs (board, i, j, word, 0)) {
                    return true;
                } 
            }
        }

        return false; 
    }

    bool dfs(vector<vector<char>>& board, int row, int col, string& word, int track) {
        
        if (track == word.size()) 
            return true; 
        if (row < 0 || col < 0 || row >= board.size() || col >= board[0].size())
            return false;
        if (word[track] != board[row][col]) 
            return false; 

        char saved = board[row][col]; 
        board[row][col] = '#';
        track++; 

        bool found =     dfs(board, row+1, col, word, track) 
                        || dfs(board, row-1, col, word, track) 
                        || dfs(board, row, col+1, word, track) 
                        || dfs(board, row, col-1, word, track);
            // something like this im imagining. 

        board[row][col] = saved; 

        return found; 

    }
};
