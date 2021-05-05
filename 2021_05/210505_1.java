// 프로그래머스 레벨2 구명보트 
import java.util.Arrays ;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Collections;

class Solution {
    public int solution(int[] people, int limit) {
        HashMap<Integer,Integer> heavyPeople = new HashMap<>();
        HashMap<Integer,Integer> lightPeople = new HashMap<>();

        for(int i : people){
            if( i <= limit/2){
                lightPeople.put(i, lightPeople.getOrDefault(i, 0) +1 );
            } else{
                heavyPeople.put(i, heavyPeople.getOrDefault(i, 0) +1 );            }
        }

        int nBoat = 0;
        ArrayList<Integer> lightWeigths = new ArrayList<>(lightPeople.keySet());
        Collections.sort(lightWeigths, Collections.reverseOrder());
        for(int i : heavyPeople.keySet()){
            int numberOfPeopleH =  heavyPeople.get(i);
            nBoat += numberOfPeopleH ;
            for(int j : lightWeigths ){
                if( i+j <= limit){
                    if(lightPeople.get(j) - numberOfPeopleH <= 0 ){
                        numberOfPeopleH -= lightPeople.get(j);
                        lightPeople.put(j, 0);
                    } else{
                        lightPeople.put(j, lightPeople.get(j)- numberOfPeopleH);
                        break;
                    }
                }
            }
        }

        int left = lightPeople.values().stream().reduce(0, Integer::sum);

        if(left %2 == 0 ){
            return nBoat + left/2 ;
        } else{
             return nBoat + left/2 +1  ;
        }

    }
}
