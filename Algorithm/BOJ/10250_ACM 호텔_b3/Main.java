// boj 10250 ACM 호텔 b3
// noj.am/10250

import java.io.*;
import java.util.*;

public class Main{
  public static void main(String[] args) throws NumberFormatException, IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine());
    for (int i = 0; i < T; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      StringBuilder sb = new StringBuilder();
      int H = Integer.parseInt(st.nextToken());
      int W = Integer.parseInt(st.nextToken());
      int N = Integer.parseInt(st.nextToken());

      // 일의 자리 = H로 나눈 몫 + 1,  백~천의 자리 = H로 나눈 나머지  1, 10, 9
      int floor = N % H;
      int roomNum = (N / H);
      if (floor == 0) {
        sb.append(H);
        if (roomNum < 10) sb.append('0');
        sb.append((roomNum));
      }else{
        sb.append(floor);
        if (roomNum + 1 < 10) sb.append('0');
        sb.append((roomNum) + 1);
      } 
      System.out.println(sb);
    }
  }
}