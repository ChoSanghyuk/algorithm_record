// 프로그래머스 
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> getMax = new ArrayList<>();
        int[] scores = {0,0,0};
        int[] answer1 = {1, 2, 3, 4, 5} ;
        int[] answer2 = {2, 1, 2, 3, 2, 4, 2, 5} ;
        int[] answer3 = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5} ;
        for(int i =0 ; i< answers.length ; i++){
            if(answers[i] == answer1[i%5]){
                scores[0] ++;
            }
            if(answers[i] == answer2[i%8]){
                scores[1] ++;
            }
            if(answers[i] == answer3[i%10]){
                scores[2] ++;
            }
        }
        int maxScore = 0 ;
        for(int i : scores){
            if(maxScore < i){
                maxScore = i;
            }
        }
        for(int i =0 ; i < scores.length ; i++){
            if(maxScore == scores[i]){
                getMax.add(i+1);
            }
        }
        int[] answer = new int[getMax.size()] ;
        for(int i =0 ; i < answer.length ; i++){
            answer[i] = getMax.get(i);
        }
      //  Integer[] answer = getMax.toArray(new Integer[getMax.size()]);
        return answer;
    }
}
