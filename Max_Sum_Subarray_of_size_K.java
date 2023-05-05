class Solution{
    static long maximumSumSubarray(int k, ArrayList<Integer> arr,int N){
        int i=0;
        int j=0;
        long a=0;
        long b=0;
        while(j<arr.size()){
            a+=arr.get(j);
            if(j-i+1==k){
                b=Math.max(a,b);
                a-=arr.get(i);
                i+=1;
            }
            
            j+=1;
        }
        return b;
    }
}
