// 프로그래머스 레벨1 두 정수 사이의 합
import java.lang.Math;
class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        for(int i =  Math.min(a,b); i <= Math.max(a,b) ; i++){
            answer += i;
        }
        return answer;
    }
}
