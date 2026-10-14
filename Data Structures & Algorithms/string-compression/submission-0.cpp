class Solution {
public:
    int compress(vector<char>& chars) {

        
        string ans = ""; 

        for (int l = 0; l < chars.size(); ) {

            ans += chars[l];    // append the chars[l] letter in first 
                                // now we need to append the count 

            int count = 0; 
            int r = l; 
            char letter = chars[l];
        
            while (r < chars.size()) {
                if (letter != chars[r]) 
                    break; // leave  
                count++; 
                r++; 
            }
            
            if (count > 1) 
                ans += to_string(count);
            count = 0; 
            l = r;
        }

        for (int i = 0; i < ans.size(); i++) {
            chars[i] = ans[i];
        }

        return ans.size(); 
        
    }
};