import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N, M;
    ArrayList<Integer> cardList = new ArrayList<>();
    int ans = 0;
    
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    st = new StringTokenizer(br.readLine());
    for(int i = 0; i < N; i++) cardList.add(Integer.parseInt(st.nextToken()));

    Collections.sort(cardList);
    
    int sum = 0;
    for (int i = 0; i < cardList.size(); i++) {
      for (int j = i + 1; j < cardList.size(); j++) {
        for (int k = j + 1; k < cardList.size(); k++) {
          sum = cardList.get(i) + cardList.get(j) + cardList.get(k);
          if (sum >= ans && sum <= M) ans = sum;
        }
      }
    }

    System.out.println(ans);
  }

}
