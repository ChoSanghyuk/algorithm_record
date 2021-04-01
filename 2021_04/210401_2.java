// 프로그래머스 레벨1 같은 숫자는 싫어
import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        int temp = -1;
        for(int i : arr){
            if(temp == i){
                continue;
            } else{
                list.add(i);
                temp = i ;
            }
        }
        
        int[] answer = new int[list.size()];
        for(int i =0 ; i< list.size() ; i++){
            answer[i] = list.get(i);
        }
        

        return answer;
    }
}
