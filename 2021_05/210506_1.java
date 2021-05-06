// 프로그래머스 레벨2 타겟 넘버
import java.util.Arrays;
class Solution {
    static int count = 0;
    public int solution(int[] numbers, int target) {
        Arrays.sort(numbers);
        int sum = 0;
        for(int i: numbers){
            sum += i;
        }
        int goal = (sum - target)/2 ;
        
        findCombination(numbers, 0, goal);
        return  count;
        
    }
    public static void findCombination( int[] numbers, int idx,int goal){
        for(int i = idx; i < numbers.length ; i++){
            int onProcess = goal - numbers[i];
            if(onProcess == 0 ){
                count++;
            } else if (onProcess < 0){
                break;
            } else{
                findCombination(numbers, i+1 ,onProcess);
            }
        }
    }

}
