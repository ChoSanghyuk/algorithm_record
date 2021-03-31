// 프로그래머스 레벨1 3진법 뒤집기
import java.lang.Math;
class Solution {
    public int solution(int n) {
        int answer = 0;
        String reverseT = "";
        while(n > 0){
            reverseT += (n % 3);
            n = (int) (n/3);
        }
        System.out.println(reverseT);
        for(int i = reverseT.length()-1 ; i>=0 ; i--){
            int temp = reverseT.charAt(i) - '0';
            answer += temp * (Math.pow(3, (reverseT.length()-1)-i ));
        }
        return answer;
    }
}


// a = new StringBuilder(a).reverse().toString();
// return Integer.parseInt(a,3);
