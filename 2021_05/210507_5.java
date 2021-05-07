// 프로그래머스 레벨2 H-Index
import java.util.Arrays;
class Solution {
    public int solution(int[] citations) {
        int hValue = 0;
        for(int h = 0 ; h <= citations.length ; h++){
            final int t = h;
            if( Arrays.stream(citations).filter(i -> i>=t).toArray().length >=h ){
                hValue = h ;
            } else{
                break;
            }
        }
        return hValue;
    }
}
