// 프로그래머스 레벨2 메뉴 리뉴얼
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Arrays;
class Solution {
    public String[] solution(String[] orders, int[] course) {
        HashSet<String> sets = new HashSet<>();
        for(int i : course){
            HashSet<String> combination = new HashSet<>();
            for(String s: orders){
                candidates(combination , s , i);
            }
            ArrayList<String> candiSet = new ArrayList<>();
            int max = 2;
            for(String s: combination){
                int isMax = isDouble(s, orders);
                if(isMax == max) {
                    candiSet.add(s);
                } else if (isMax > max ){
                    max = isMax;
                    candiSet.clear();
                    candiSet.add(s);
                }
            }
            for(String s : candiSet){
                char[] temp = s.toCharArray();
                Arrays.sort(temp);
                sets.add(new String(temp));
            }
            
        }
           
        String[] answer = new String[sets.size()];
        sets.toArray(answer);
        Arrays.sort(answer);
        return answer;
    }
    public static void candidates(HashSet<String> combination, String order,int n){
        if(order.length() == n){
            combination.add(order);
            return ;
        }
        for(int i = 0 ; i< order.length(); i++ ){
            String temp = order.substring(0, i) + order.substring(i+1);
            if(temp.length() == n){
                combination.add(temp);
            }
            else{
                candidates(combination , temp, n);
            }
        }
    }
    public static int isDouble(String combo , String[] orders){
        int count = 0;
        for(String s: orders){
            boolean inMenu = true;
            for(char c : combo.toCharArray()){
                if(s.indexOf(c) == -1){
                    inMenu = false;
                }
            }
            if(inMenu){
                count++;
            }
        }
        return count ;
    }
}
