// 프로그래머스 레벨2 위장
import java.util.HashMap;
class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> combination = new HashMap<>();
        for(String[] sList : clothes){
            combination.put(sList[1] , combination.getOrDefault(sList[1], 0)+1);
        }
        int answer = 1;
        for(int i : combination.values()){
            answer *= (i+1);
        }
        return answer-1;
    }
}
