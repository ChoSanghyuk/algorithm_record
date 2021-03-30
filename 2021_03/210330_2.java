// 프로그래머스 레벨1 2016년
class Solution {
    public String solution(int a, int b) {
        String[] months = {"FRI","SAT","SUN","MON","TUE","WED","THU"};
        int[] days = {31,29,31,30,31,30,31,31,30,31,30,31};
        int numDays = 0;
        for(int i =1 ; i < a ; i++){
            numDays += days[i-1];
        }
        numDays += (b-1);
        return months[numDays % 7];
    }
}
