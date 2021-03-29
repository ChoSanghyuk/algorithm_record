// 프로그래머스 신규 아이디 
class Solution {
    public String solution(String new_id) {
        new_id = new_id.toLowerCase();
        String temp = "";
        for (char i : new_id.toCharArray()){
            boolean ok = true;
            for(char j : "~!@#$%^&*()=+[{]}:?,<>/".toCharArray()){
                if(i==j){
                    ok = false;
                    break;
                }
            }
            if(ok){
                temp += i;
            }
        }
        new_id = temp;
        temp ="" ;
        boolean before = false;
        for(char i : new_id.toCharArray()){
            if( (i =='.') && before){
                continue;
            } else if (i == '.'){
                before = true;
            } else{
                before = false;
            }
            temp += i;
        }
        new_id = temp;

        if (new_id ==""){
            new_id += 'a';
        }
        int start = 0 , end = new_id.length() ;
        if(new_id.indexOf('.')==0){
            start ++;
        }
        if(new_id.lastIndexOf('.') == new_id.length()-1){
            end --;
        }
       
        if( (start < end) && (start < new_id.length())){
            new_id = new_id.substring(start, end);
        } else {
            new_id ="a";
        }
        if (new_id ==""){
            new_id += 'a';
        }
        
        System.out.println(new_id);
        
        if(new_id.length() >=16){
            if(new_id.charAt(14) == '.'){
                new_id = new_id.substring(0,14);
            } else{
                new_id = new_id.substring(0,15);
            }
        } else if ( new_id.length() <=2){
            while(new_id.length() <=2){
                new_id += new_id.charAt(new_id.length()-1);
            }
        }
        
        return new_id;
        
    }
}
