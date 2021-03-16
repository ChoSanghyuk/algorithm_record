// 프로그래머스 크레인 인형 뽑기
import java.util.ArrayList;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer =0;
        ArrayList<Integer> dolls = new  ArrayList<Integer>();
        dolls.add(0);
        for(int i : moves){
            for(int[] j : board){
                if(j[i-1]==0){
                    continue;
                }else{
                    if(dolls.get(dolls.size()-1) == j[i-1] ){
                        dolls.remove(dolls.size()-1);
                        answer +=2;
                    }
                    else{
                        dolls.add(j[i-1]);
                    }
                    j[i-1]=0;
                    break;
                }
                
            }
        }
        
        return answer;
    }
}
