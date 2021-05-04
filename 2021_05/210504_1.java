// 프로그래머스 레벨2 조이스틱

class Solution {
    public int solution(String name) {
        
        int move = 0 , len = name.length() ; 
        for(int i = 0; i< len ; i++ ){
            move += Math.min( name.charAt(i) - 'A' , ('Z' - name.charAt(i)) +1 );
        }
        int minMove = len -1;
        for(int i = 0 ; i < len -1 ; i++){
            if(name.charAt(i + 1) == 'A'){
                int t = i +1;
                while(t<len){
                    if(name.charAt(t) != 'A'){
                        break;
                    }
                    t++;
                }
                minMove = Math.min(minMove, len - t + i*2 );
            }
        }
        return move + minMove ;
       
            
    }
    


}
