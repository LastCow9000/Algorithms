// boj 2751 수 정렬하기 2
// noj.am/2751

import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int N = Integer.parseInt(br.readLine());
    ArrayList<Integer> numList = new ArrayList<>();
    while (N-- > 0) numList.add(Integer.parseInt(br.readLine()));
    numList.stream().sorted().forEach(ans ->{
      try{
        bw.write(String.valueOf(ans));
        bw.write('\n');
      }catch(IOException e){
        throw new UncheckedIOException(e);
      }
    });

    bw.flush();
    bw.close();
    br.close();

  }
}
