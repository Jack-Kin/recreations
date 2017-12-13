package com.junlonga.app.problem_311;

/**
 * Created by junlonga on 7/24/2016.
 */

public class P311 {
        public int[][] multiply(int[][] A, int[][] B) {
            int m = A.length, n = A[0].length, p = B[0].length;
            int[][] C = new int[m][p];

            for(int i = 0; i < m; i++){
                for(int j = 0; j < n; j++){
                    if(A[i][j] == 0) continue;
                    for(int k = 0; k < p; k++){
                        if(B[j][k] == 0) continue;
                        C[i][k] += A[i][j]*B[j][k];
                    }
                }
            }

            return C;
    }
}
