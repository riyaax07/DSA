class Solution {
    public void setZeroes(int[][] matrix) {
        int r = matrix.length;
        int c= matrix[0].length;
        boolean fri= false;
        boolean fci = false;

        for(int col=0;col<r;col++){
            if (matrix[col][0]==0){
                fci = true;
                break;
            }
        }
        for(int row=0;row<c;row++){
            if (matrix[0][row]==0){
                fri = true;
                break;
            }
        }
        for(int i=1;i<r;i++){
            for(int j=1;j<c;j++){
                if(matrix[i][j]==0){
                    matrix[i][0]=0;
                    matrix[0][j]=0;
                }
            }
        }
        for(int i=1;i<r;i++){
            for(int j=1;j<c;j++){
                if(matrix[0][j]==0 || matrix[i][0]==0){
                    matrix[i][j]=0;
                }
            }
        }
        if(fri){
            for(int j=0;j<c;j++){
                matrix[0][j]=0;
            }
        }
        if(fci){
            for(int i=0;i<r;i++){
                matrix[i][0]=0;
            }
        }
    }
}