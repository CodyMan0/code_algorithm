const solution = (common) => {

  if (Math.sign(common[0])=== -1) {
      if(common[2] % common[1] === 0) return common[0]**(common.length+1)
    const dif = common[1] - common[0]
    console.log(dif)
    return common[0]+dif*(common.length) 
    }

    
if (common[0] === 1){
    if(common[2] % common[1] === 0) return common[1]**(common.length)
    const dif = common[2] -common[1]
    return common[0]+dif*(common.length)
} 
    
    if(common[1] % common[0] === 0) return common[0]**(common.length+1)
    const dif = common[2] -common[1]
    return common[0]+dif*(common.length) 

  


    
}