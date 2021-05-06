//프로그래머스 레벨2 더 맵게
import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int count = 0;
        PriorityQueue<Integer> foods = new PriorityQueue<>();
        for(int i : scoville){
            foods.add(i);
        }
        
        while(foods.peek() < K){
            int ingredient1 = foods.poll();
            Integer ingredient2 = foods.poll();
            if(ingredient2 == null){
                return -1;
            }
            foods.add(ingredient1 + ingredient2*2 );
            count++;
        }
        return count;
        
    }
}
