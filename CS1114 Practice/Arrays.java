//Arrays
//Count Zero Rows
public static int zeroRows(int[][] grid){
    int count = 0;

    for(int x = 0; x < grid.length; x++){
        boolean allZero = true;
        for(int y = 0; y < grid[x].length; y++){
            if (grid[r][c] != 0){
                allZero = false;
                break;
            }
        }
        if (allZero){
            count++;
        }
    }
    return count;
}

//Sum All elements
    public static int sum2d(int[][]arr){
        int sum = 0;
        for(int x = 0; x < arr.length; x++){
            for(int y = 0; y < arr[x].length; y++){
                sum += arr[x][y];''
            }
        }
        return sum;
    }

    //max in row
    public static int maxInRow(int[][] arr, int row){
        int max = arr[row][0]
        for(int x = 0; x < arr[row].length; x++){
            if(arr[row][x] > max){
                max = arr[row][x];
            }
        }
        return max;
    }

    //count zero
    public static int countZero(int[][] grid){
        int count = 0; 
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] == 0) {
                    count++;
                }
            }
        }
        return count;
    }