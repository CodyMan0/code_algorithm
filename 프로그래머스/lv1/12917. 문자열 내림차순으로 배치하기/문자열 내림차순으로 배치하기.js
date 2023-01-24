function solution(s) {
   return s.split("").map(x => x.charCodeAt()).sort((a,b) => b-a).map(x => String.fromCharCode(x)).join("")  
}