class Solution {
    public int solution(int[] nums) {
        HashSet<Integer> sets = new HashSet<>();
        for( Integer i : nums){
            sets.add(i);
        }
          
        if( (nums.length/2) <= sets.size() ){
            return nums.length/2;
        } else{
            return sets.size();
        }
        
    }
}
