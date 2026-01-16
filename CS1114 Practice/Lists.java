//List:
//Remove all occureneces   
public static void removeAll(List<Integer> list, int target){
    for(int i = 0; i < list.size(); i++){
        if(list.get(i) == target){
            list.remove(i);
            i--;
        }
    }
}

//Pairwise Sum
public static List<Integer> pairwiseSum(List<Integer> nums){
    List<Integer> result = new ArrayList<>();

    for(int i = 0; i < nums.size(); i++){
        int sum = nums.get(i) + nums.get(i+1);
        result.add(sum);
    }
    return result;
}

//Replace Negatived With zero
public static void fixNegatives(List<Integer> nums) {
    for(int i = 0; i < nums.size(); i++){
        if(nums.get(i) < 0){
            nums.set(i, 0);
        }
    }
}

//DOUBLE all values:
    public static List<Integer> doubleValues(List<Integer> nums){
        List<Integer> result = new ArrayList<>();
        for (int n : nums){
            result.add(n*2)
        }
        return result;
    }

    //Remove long words:
    public static void removeLongWords(List<String> words) {
        for(int i = 0; i< words.size(); i++){
            if (words.get(i).length() > 5){
                words.remove(i);
                i--;
            }
        }
    }

    //Count Occurences
    public static int countOccurences(List<String> list, String target){
        int count = 0;
        for (String s : list){
            if(s.equals(target)){
                count++
            }
        }
        return count;
    }