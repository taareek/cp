// Hacker rank problem: Between two sets 
// https://www.hackerrank.com/challenges/between-two-sets/problem



int getTotalX(vector<int> a, vector<int> b) {
    // sorting array b to get the minimum element
    sort(b.begin(), b.end());
    int cnt=0;
    for(int i=1; i<=b[0]; i++){
        bool is_fact_b = true;
        for(auto itb:b)
            if(itb % i !=0){
                is_fact_b = false;
                break;
            }
        if(is_fact_b){
            bool is_i_mul_a = true;
            for(auto ita:a)
                if(i % ita !=0){
                    is_i_mul_a = false;
                    break;
                }
            if(is_i_mul_a){
                cnt++;
            }
        }
            
    }
    return cnt;
}