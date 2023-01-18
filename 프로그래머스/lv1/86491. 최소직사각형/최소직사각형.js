function solution(sizes) {
    const copy = [...sizes];
    const sortedCopy = copy.map((el)=>{
        return sort = el.sort((a,b) => (a-b)) 
    })
    const pickOneFromBig = sortedCopy.map((el) => {
        return el[0]
    })
    
     const pickOneFromSmall = sortedCopy.map((el) => {
        return el[1]
    })
     
     return Math.max(...pickOneFromBig) * Math.max(...pickOneFromSmall)
}
