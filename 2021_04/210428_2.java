// 프로그래머스 level 2 다리를 지나는 트럭
import java.util.ArrayList;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {

        int time = 1 ,  next = 1;
        ArrayList<Truck> trucksOnBridge = new ArrayList<>();
        trucksOnBridge.add(new Truck(1, truck_weights[0]));

        while( next < truck_weights.length){
            time++;

            // 나갈 트럭 여부 결정
            if( time == trucksOnBridge.get(0).getStartTime() + bridge_length ){
                trucksOnBridge.remove(0);
            }

            // 들어올 트럭 여부 결정
            int totalWeight = 0;
            for(Truck truck : trucksOnBridge){
                totalWeight += truck.getWeight();
            }
            if(totalWeight+ truck_weights[next] <= weight ){
                trucksOnBridge.add(new Truck(time, truck_weights[next]));
                next++  ;
            }
        }

        return time + bridge_length ;
    }

    class Truck {
        int startTime;
        int weight;

        Truck(int startTime, int weight){
            this.startTime = startTime;
            this.weight = weight;
        }
        public int getStartTime(){
            return startTime;
        }
        public int getWeight(){
            return weight;
        }
    }
}
