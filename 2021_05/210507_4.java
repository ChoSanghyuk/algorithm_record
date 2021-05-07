// 프로그래머스 레벨2 카펫
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        for(int i = (int) Math.sqrt(yellow) ; i<= yellow ; i++ ){
            if(i>= yellow/i && (int) yellow/i == yellow/i 
                            && 2*(i+ (yellow/i)+2) == brown ){
                answer[0] = i+2 ; answer[1] = ((int)yellow/i)+2 ;
                break;
            }
        }
        return answer;
    }
}
