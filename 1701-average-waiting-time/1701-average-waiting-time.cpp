class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        double waiting = 0;
        int last_finish = customers[0][0];
        for (int i = 0; i < customers.size(); i++){
            int extra_time = 0;
            int arrival = customers[i][0];
            int time = customers[i][1];

            if (last_finish <= arrival){
                waiting += time;
                last_finish = arrival + time;
            }
            else{
                extra_time = last_finish - arrival;
                waiting += time + extra_time;
                last_finish += time;
            }
        }
        return waiting / customers.size();    
    }
};