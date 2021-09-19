// boj 10845 큐 s4
// noj.am/10845

import java.io.*;
import java.util.*;

public class Main{
  public static void main(String[] args) throws NumberFormatException, IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    Queue q = new Queue();

    while (N-- > 0){
      StringTokenizer st = new StringTokenizer(br.readLine());
      String cmd = st.nextToken();
      int num = 0;
      if (st.hasMoreTokens()){
        num = Integer.parseInt(st.nextToken());
        q.push(num);
      }
      else if (cmd.equals("pop")) System.out.println(q.pop());  
      else if (cmd.equals("size")) System.out.println(q.size()); 
      else if (cmd.equals("empty")) System.out.println(q.empty());
      else if (cmd.equals("front")) System.out.println(q.front());
      else if (cmd.equals("back")) System.out.println(q.back());
    }
  }
}

class Queue{
  private LinkedList<Integer> list = new LinkedList<>();

  public void push(int num){
    this.list.add(num);
  }

  public int pop(){
    return this.list.size() != 0 ? this.list.removeFirst() : -1;
  }

  public int size(){
    return this.list.size();
  }

  public int empty(){
    return this.list.size() == 0 ? 1 : 0;
  }

  public int front(){
    return this.list.size() != 0 ? this.list.getFirst() : -1;
  }
  public int back(){
    return this.list.size() != 0 ? this.list.getLast() : -1;
  }
}