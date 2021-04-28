// 프로그래머스 level2  124 나라의 숫자
class Solution {
    public String solution(int n) {
        StringBuilder sb = new StringBuilder();
        while(n> 0){
            if( n% 3 == 0 ){
                sb.append(4);
                n = n/3 - 1;
            } else {
                sb.append(n%3);
                n /= 3;
            }
        }
        if( sb.charAt(0) == '0'){
            sb.deleteCharAt(0);
        }
        return sb.reverse().toString();
    }
}
