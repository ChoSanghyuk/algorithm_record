// 프로그래머스 레벨1 체육복
import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Map<Integer, Integer> members = new HashMap<>();
        for(int i =1 ; i <= n ; i++){
            members.put(i,1);
        }
        for(int i : lost){
            members.replace(i, 0);
        }
        
        Arrays.sort(reserve);
        for(int i : reserve){
            if( members.get(i) == 0){
                members.replace(i,1);
                continue;
            } 
           
            if( i>1 && members.get(i-1) == 0){
            members.replace(i-1, 1);
            continue;
            } 
           
            if( i<n && members.get(i+1) == 0 && (Arrays.binarySearch(reserve, i+1) <0) ){
            members.replace(i+1, 1);
            continue;
            } 
          
        }
        int answer = 0;
        for(Integer i : members.keySet()){
            answer += members.get(i);
        }
        return answer;
    }
}
