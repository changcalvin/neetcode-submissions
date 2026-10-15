class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {    

        unordered_map<string, vector<string>>   emailToEmails; 
        unordered_map<string, string>           emailToName;
        vector<vector<string>> preSortedAns; 


        fillInMaps(accounts, emailToEmails, emailToName);    
        runBFS(preSortedAns, emailToEmails, emailToName); 
        sortAns(preSortedAns);

        return preSortedAns; 

    }

    void sortAns(vector<vector<string>>& preSortedAns) {
        for (auto& accounts : preSortedAns) {
            sort(accounts.begin() + 1, accounts.end()); 
        }
    }

    void runBFS(vector<vector<string>>& preSortedAns, 
                unordered_map<string, vector<string>>& emailToEmails,
                unordered_map<string, string>& emailToName) {
        
        unordered_set<string> seen; 

        for (const auto& [email, neighbors] : emailToEmails) {
            if (seen.contains(email)) continue; 

            vector<string> entry;
            entry.push_back(emailToName[email]);

            queue<string> q; 
            q.push(email);
            seen.insert(email);

            while (!q.empty()) {
                string curr = q.front();
                q.pop();
                entry.push_back(curr);

                for (const auto& neighbor : emailToEmails[curr]) {
                    if (!seen.contains(neighbor)) {
                        seen.insert(neighbor);
                        q.push(neighbor);
                    }
                }
            }
            preSortedAns.push_back(entry);   
        }
        // first we begin with the first email on emailToEmails 
    }

    void 
    fillInMaps(vector<vector<string>>& accounts, 
                unordered_map<string, vector<string>>& emailToEmails,
                unordered_map<string, string>& emailToName) {
        
        for (const auto& account : accounts) {
            const string& name      = account[0];
            const string& anchor    = account[1];

            emailToName[anchor] = name;
            emailToEmails[anchor];


            for (int i = 2; i < account.size(); i++) {
                emailToName[account[i]] = name;

                emailToEmails[anchor].push_back(account[i]);
                emailToEmails[account[i]].push_back(anchor);
            }
        }
        
   }
};