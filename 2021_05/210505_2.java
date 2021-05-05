// 프로그래머스 레벨2 소수 찾기
import java.util.ArrayList;
import java.util.HashSet;
import java.util.stream.Collectors;

class Solution {
    public int solution(String numbers) {
        char[] charIndex = {'0', '1', '2','3','4','5','6','7','8','9'};
        int answer = 0;
        ArrayList<String> combination = new ArrayList<>();
        for(int i=0 ; i< numbers.length() ; i++){
            combination.add("" + i);
        }
        int end = 0;
        for(int i = 1 ; i < numbers.length() ; i++ ){
            int begin = end;
            end = combination.size();
            for(int j = begin ; j < end ; j++ ){
                for(int t = 0 ; t < numbers.length() ; t++){
                    if(combination.get(j).indexOf(charIndex[t]) == -1 ){
                        String newIndex = combination.get(j) + t;
                        combination.add(newIndex );
                    }
                }
            }
        }
        HashSet<Integer> combiSet = new HashSet<>();
        for(String str : combination ){
            String convert = "";
            for(int i = 0 ; i < str.length() ; i++){
                convert += numbers.charAt(Integer.parseInt(""+str.charAt(i)));
            }
            combiSet.add(Integer.parseInt(convert));
        }

        for(int i : combiSet){
            if(isPrime(i)){
                answer++;
            }
        }
        return answer;
    }
    public static boolean isPrime(int number){
        if(number == 2 ){
            return true;
        } else if ( number==0 || number == 1 || number%2==0){
            return false;
        }
        for(int i =3; i < number/2 ; i+=2){
            if(number%i==0){
                return false;
            }
        }
        return true;
    }
}
