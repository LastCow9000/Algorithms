/* 
2017 카카오코드 본선 리틀 프렌즈 사천성 lv3
https://programmers.co.kr/learn/courses/30/lessons/1836
*/

import java.util.*;

public class Solution{

    char[][] board;
    ArrayList<Character> list = new ArrayList<>();
    HashMap<Character, int[][]> map = new HashMap<>();

    public String solution(int m, int n, String[] board) {
        String ans = "";
        this.board = new char[m][n];

        for(int i = 0; i < m; i++){
            for (int j = 0;j < n;j++){
                char tmp = board[i].charAt(j);
                this.board[i][j] = tmp; // 문자 하나하나씩 쉽게 다루기 위해 char 배열로 전환
                if (tmp >= 'A' && tmp <= 'Z'){ // 문자면
                    if (!list.contains(tmp)){ // 처음 들어가는 문자면 찾을 리스트에 저장
                        list.add(tmp);
                        map.put(tmp, new int[2][2]);
                        map.get(tmp)[0][0] = i;
                        map.get(tmp)[0][1] = j;
                    }else{
                        map.get(tmp)[1][0] = i;
                        map.get(tmp)[1][1] = j;
                    }
                }
            }
        }

        Collections.sort(list);

        int idx = 0;
        while (list.size() != 0){ // 리스트가 빌 때까지
            if (checkDel(list.get(idx))){
                char alpha = list.remove(idx);
                int[][] pos = map.get(alpha);
                this.board[pos[0][0]][pos[0][1]] = '.'; // 삭제후 . 으로 변경
                this.board[pos[1][0]][pos[1][1]] = '.';
                ans += alpha;
                idx = 0;
            }else{
                idx += 1;
                if(idx == list.size()) return "IMPOSSIBLE"; // 리스트 크기 만큼 돌았으면 다 돌았으므로
            }
        }

        return ans;
    }

    boolean seroCheck(int r1, int r2, int col, char c){
        for (int i = r1; i <= r2 ; i++){
            if (board[i][col] != '.' && board[i][col] != c) return false;
        }
        return true;
    }

    boolean garoCheck(int c1, int c2, int row, char c){
        for (int i = c1; i <= c2 ; i++){
            if (board[row][i] != '.' && board[row][i] != c) return false;
        }
        return true;
    }

    boolean checkDel(char c){
        int r1 = map.get(c)[0][0];
        int r2 = map.get(c)[1][0];
        int c1 = map.get(c)[0][1];
        int c2 = map.get(c)[1][1];

        if (c1 < c2){
            if (seroCheck(r1, r2, c1, c) && garoCheck(c1, c2, r2, c)) return true;
            if (seroCheck(r1, r2, c2, c) && garoCheck(c1, c2, r1, c)) return true;
        }else {
            if (seroCheck(r1, r2, c1, c) && garoCheck(c2, c1, r2, c)) return true;
            if (seroCheck(r1, r2, c2, c) && garoCheck(c2, c1, r1, c)) return true;
        }

        return false;
    }
}

class Test{
    public static void main(String[] args) {
        Solution t = new Solution();
        int m = 3;
        int n = 3;
        String[] board = {"DBA", "C*A", "CDB"}; //"ABCD"
        System.out.println(t.solution(m, n, board));
}
}
/*
1. 알파벳이면 같은 행이나 같은 열에 장애물(*, 다른블록)없이 같은 알파벳이 있는지
2.  `.` 이면 자신의 행이나 자신의 열에서 같은게 있는지 확인
3. `*`이면 검사x
*/



