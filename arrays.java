class arrays{
    public static void main(String[]args){

        int[] nums = {10,22,45,688,787,160};

        System.out.println(nums[2]);        
        nums[2] = 57;
        System.out.println(nums[2]);        
        

        for(int i=0;i<=nums.length;i++){
            System.out.println(nums[i]);
        }

    }
}