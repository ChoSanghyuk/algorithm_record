// 프로그래머스 두 개 뽑아서 
import java.util.Set;
import java.util.TreeSet;

class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> sets = new TreeSet<>();
        for(int i =0; i< numbers.length-1; i++){
            for(int j = i+1 ; j < numbers.length; j++){
                sets.add( numbers[i] + numbers[j]);
            }
        }
        int[] answers = new int[sets.size()];
        int k=0;
        for(Integer i : sets){
            answers[k++] = i;
        }
        return answers;
    }
    
}
