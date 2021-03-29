// 프로그래머스 레벨1 K번째 수
import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        System.out.println(answer.length);
        int num = 0;
        for(int[] arr : commands){
            int[] temp = new int[arr[1] - arr[0] +1];
            temp = Arrays.copyOfRange(array, arr[0]-1, arr[1]);
            Arrays.sort(temp);
            answer[num] = temp[arr[2]-1];
            num++;
        }
        return answer;
    }
}
