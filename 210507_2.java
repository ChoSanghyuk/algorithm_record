// 프로그래머스 레벨2 큰 수 만들기
class Solution {
    public String solution(String number, int k) {
        return addMaxChar(number, k );
    }
    public static String addMaxChar(String number ,int upToIdx){
        if(number.length() == upToIdx){
            return "";
        }
        char max = '0' ; int idx = -1;
        for(int i = 0 ; i <= upToIdx ; i++){
            if(max < number.charAt(i) ){
                max = number.charAt(i);
                idx = i;
            }
        }
        if(idx == upToIdx){
            return number.substring(idx);
        } else{
            return max + addMaxChar(number.substring(idx+1) , upToIdx - idx);
        }
    }
}
