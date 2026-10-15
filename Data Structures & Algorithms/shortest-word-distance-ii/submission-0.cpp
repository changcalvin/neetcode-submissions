class WordDistance {
public:
    unordered_map<string, vector<int>> dict;

    WordDistance(vector<string>& wordsDict) {

        for (int i = 0; i < wordsDict.size(); i++) {
            dict[wordsDict[i]].push_back(i); 
        }
        
    }
    
    int shortest(string word1, string word2) {
        const vector<int>& vec1 = dict[word1];
        const vector<int>& vec2 = dict[word2];

        int i = 0; 
        int j = 0; 
        int minDistance = INT_MAX; 

        while (i < vec1.size() && j < vec2.size()) {
            minDistance = min(minDistance, abs(vec1[i]-vec2[j]));
            if (vec1[i] > vec2[j]) {
                j++; 
            } else {
                i++;
            }
        }

        return minDistance; 
        
    }
};

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance* obj = new WordDistance(wordsDict);
 * int param_1 = obj->shortest(word1,word2);
 */
