// 프로그래머스 레벨1 가운데 글자
class Solution {
    public String solution(String s) {
        String answer = "";
        int length = s.length();
        if(length % 2 == 0){
            int index = length/2 ; 
            answer = answer + s.charAt(index-1) + s.charAt(index);
        } else{
            int index = length/2;
            answer += s.charAt(index);
        }
        return answer;
    }
}
