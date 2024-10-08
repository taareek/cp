// https://www.hackerrank.com/challenges/the-birthday-bar/problem

// logic 
int birthday(vector<int> s, int d, int m) {
    int ways = 0;
    
    for(int i =0; i<s.size(); i++){
        int length = 0;
        for(int k=i; k<i+m; k++){
            length += s[k];
        }
        if(length == d){
            ways++;
        }
    }
    return ways;
}