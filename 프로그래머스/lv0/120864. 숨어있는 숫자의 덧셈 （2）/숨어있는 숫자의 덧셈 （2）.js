function solution(my_string) {

    
    
    return my_string.split(/[^0-9]/).filter(i=>i).reduce((prev,acc) => {
        return prev + (+acc)
    },0)
}