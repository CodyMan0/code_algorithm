import copy

def solution(priorities, location):
    answer = 0
    wait_list_queue =  [(i,p) for i,p in enumerate(priorities)]

    while True: 
        cur = wait_list_queue.pop(0)
        print(q[1] for q in wait_list_queue)
        if any(cur[1] < q[1] for q in wait_list_queue):
            wait_list_queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

    