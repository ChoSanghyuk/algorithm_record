// 프로그래머스 레벨2 기능개발
import java.util.Stack;
import java.util.ArrayList;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Stack<Integer> stack = new Stack<>();
        ArrayList<Integer> list = new ArrayList<>() ;
        for(int i = progresses.length -1 ; i >=0 ; i--){
            stack.push(progresses[i]);
        }
        int dayPassed = 1 , idx = 0;
        while(!stack.empty()){
            
           if(stack.peek() + speeds[idx] * dayPassed >= 100){
               int count = popStack(stack, dayPassed, idx, speeds);
               list.add(count);
               idx+= count;
           }
            dayPassed++;
        }
        int[] answer = new int[list.size()];
        for(int i=0 ; i < list.size() ; i++ ){
            answer[i] = list.get(i);
        }
        return answer;
    }
    public static int popStack(Stack<Integer> stack, int dayPassed , int idx, int[] speeds ){
        int count = 0;
        while(stack.peek() + dayPassed*speeds[idx] >= 100 ){
            stack.pop();
            count++;
            idx++;
            if(stack.size()==0){
                break;
            }
        }
        return count;
    }
}
