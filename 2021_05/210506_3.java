// 프로그래머스 레벨2 가장 큰 수
import java.util.ArrayList;
import java.util.Collections;
class Solution {
    public String solution(int[] numbers) {
        ArrayList<String> list = new ArrayList<>();
        for(int i : numbers){
            list.add((""+ i));
        }
        Collections.sort(list, (s1,s2) -> (s2+s1).compareTo(s1+s2) );
        String answer = "";
        for(String s : list){
            answer += s;
        }
        if(answer.replaceAll("0","").isEmpty()){
            return "0";
        }
        return answer;
    }
}
