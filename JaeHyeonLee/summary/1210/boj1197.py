"""
최소신장트리 기초 문제

크루스칼 알고리즘
간선의 가중치를 최소화

1. 가중치가 낮은 간선부터 뽑아보자(가중치 낮은 순 정렬)
2. 마냥 뽑으면 안된다. 사이클이 발생하면 그 간선은 제외(뽑아서 연결을 시켜보고: 루트노드가 같은지 판단)
2-1 union 연산, find 연산으로 판단
3. V - 1개 뽑으면 됨(트리니까)

"""