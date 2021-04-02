// 프로그래머스 레벨1 나누어 떨어지는 숫자 배열
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> list = new ArrayList<>();
        for(int i : arr){
            if( (i%divisor) == 0){
                list.add(i);
            }
        }
        if ( list.size() == 0 ){
            int[] answer = {-1};
            return answer;
        }
        int[] answer = new int[list.size()];
        for(int i =0 ; i< answer.length ; i++){
            answer[i] = list.get(i);
        }
        Arrays.sort(answer);
        return answer;
    }
}
