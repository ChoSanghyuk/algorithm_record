// 프로그래머스 레벨1 문자열 내 마음대로 정렬하기
import java.util.Arrays;
class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, (s1, s2)-> {
            if( s1.charAt(n) > s2.charAt(n)){
                return 1;
            } else if ( s1.charAt(n) < s2.charAt(n) ){
                return -1;
            } else{
                return s1.compareTo(s2);
            }
        } );
        
        return strings;
    }
}
