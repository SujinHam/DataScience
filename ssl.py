# 202103670 철학과 함수진
#Node 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#LinkedList 클래스 정의
class LinkedList:
    #초기화 메소드
    def __init__(self):
        dummy = Node(None)
        self.head = dummy
        self.tail = dummy
        self.current = None
        self.before = None
        self.num_of_data = 0

     #append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)  
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.num_of_data += 1

    # delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

            #중요 : curren가 next가 아닌 before로 변경된다.
            self.before.next = self.current.next
            self.current = self.before

            self.num_of_data -= 1
            return pop_data

    #first 메소드(search1 - 맨 앞의 노드 검색, before, current 변경)
    def first(self):
        #데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
        if self.num_of_data == 0:
            return None
       
        self.before = self.head
        self.current = self.head.next

        return self.current.data

    #next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    #size 메소드
    def size(self):
        return self.num_of_data

    #head부터 tail까지 각 노드를 순차적으로 탐색하며 각 노드의 data를 print
    def traverse_all(self):
        current_node = self.head.next
        print("head -> ", end="")
        while current_node:
            print(f"({current_node.data}) -> ", end="")
            current_node = current_node.next
        print("null")
       
     # 리스트에서 주어진 key와 일치하는 노드와 그 이전 노드를 반환
    def getNode(self, key):
        node = self.head
        before = None
        while node is not None and node.data != key:
            before = node
            node = node.next
        return before, node

    # 리스트의 주어진 위치에 new_data를 삽입
    def insert_at(self, position, new_data):
        if position<=0:
            print("Error: Invalid position")
        elif position>self.size():
            self.append(new_data)
        else:
            new_node=Node(new_data)
            if position==1:
                new_node.next=self.head
                self.head=new_node
            else:
                current=self.head
                for i in range(position-2):
                    current=current.next
                new_node.next=current.next
                current.next=new_node
            self.num_of_data+=1

    # 리스트에서 주어진 key와 일치하는 노드를 삭제
    def remove(self, key):
        if self.head is None:
            print("해당하는 원소가 없습니다.")
            return
        current = self.head
        prev = None
        index = 0
        
        while current and current.data != key:
            prev = current
            current = current.next
            index += 1
        if current:
            if prev is None:
                self.head = current.next
            else:
                prev.next = current.next
            print(f"{index}번째 원소({key})를 삭제합니다.")
        else:
            print(f"{index}번째 원소({key})를 삭제합니다.")
