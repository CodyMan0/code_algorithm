function solution(n) {

    for ( let i = 1; i < 100; i ++ ) {
        n /= i
        if(n < 1) {
            return i-1 
        }
    }
}