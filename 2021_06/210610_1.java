// 프로그래머스 레벨2 해시 전화번호 목록
import java.util.Arrays;
class Solution {
    public boolean solution(String[] phone_book) {
        
        Arrays.sort(phone_book);
        
        for(int i = 0 ; i < phone_book.length -1 ; i++){
            for( int j = i+1 ; (j < phone_book.length) ; j++ ){
                String s1 = phone_book[i] , s2=phone_book[j];
                int min = Math.min(s1.length() , s2.length());
                if(s1.substring(0,min).matches(s2.substring(0,min))) {
                    return false;
                } else{
                    break;
                }
            }
        }
        
        
        return true;
    }
}

