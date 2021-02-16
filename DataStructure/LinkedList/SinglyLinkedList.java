package LinkedList;

class LinkedList {
  Node header; // 헤더 노드 선언

  static class Node {
    int data; // 각 노드는 데이터를 가지고 있다.
    Node next = null; // 다음 노드의 주소 값(마지막 노드는 null)
  }

  LinkedList() { // 생성자
    header = new Node(); // 헤더 노드 생성
  }

  // 맨 마지막에 데이터 추가
  void append(int d) {
    Node end = new Node(); // 마지막 노드
    end.data = d; // 마지막 노드의 값
    Node n = header; // 포인터 생성
    // 맨 마지막 노드를 찾기위해 돈다.
    while (n.next != null) {
      n = n.next; // 다음 노드로 계속 이동
    }
    n.next = end; // 마지막 노드에 새로 생성한 값을 넣어준다. (새로운 얘는 맨 마지막 값이 된다.)
  }

  void delete(int d) {
    Node n = header; // 임의의 포인터 생성
    while (n.next != null) { // 첫 노두부터 마지막 노드까지 돌면서 삭제할 값을 찾는다
      if (n.next.data == d) { // 이전 노드에서 다음노드를 판별하므로 .next이다
        n.next = n.next.next; // 다음 노드는 사라지고 다다음 노드의 주소로 할당된다.
      } else {
        n = n.next; // 삭제할 노드를 못찾았을 경우 계속 찾는다.
      }
    }
  }

  // LL에 어떤 값들이 있는지 빼오는 메서드
  void retrieve() {
    Node n = header.next; // 처음부터 찾기 위한 포인터 선언
    while (n.next != null) { // 마지막 이전 노드까지 돈다.
      System.out.print(n.data + " -> ");
      n = n.next;
    }
    System.out.println(n.data); // (위의 반복문에서 마지막 이전 노드에서 반복문을 빠져나오므로) 마지막 노드 출력
  }
}

public class SinglyLinkedList {
  public static void main(String[] args) {
    LinkedList ll = new LinkedList();
    ll.append(1);
    ll.append(2);
    ll.append(3);
    ll.append(4);
    ll.retrieve();
    ll.delete(1);
    ll.retrieve();
  }

}