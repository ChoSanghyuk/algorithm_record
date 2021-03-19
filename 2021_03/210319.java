// 프로그래머스 level 1 완주하지 못한 선수

import java.util.Map;
import java.util.HashMap;
class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> dict = new HashMap<>();
        for(String i : participant){
            if(dict.containsKey(i)){
                dict.replace(i, dict.get(i)+1);
            }
            else{
                dict.put(i,1);
            }
        }
        for(String i : completion){
            dict.replace(i, dict.get(i)-1);
        }
        for(String i : dict.keySet()){
            if(dict.get(i)!=0){
                return i;
            }
        }
        return "";
    }
}

// 다른 사람 풀이
//for (String player : participant) hm.put(player, hm.getOrDefault(player, 0) + 1);  => replace를 해주지 않아도 put을 해주면 뒤에꺼 들어감
//for (String player : completion) hm.put(player, hm.get(player) - 1);
