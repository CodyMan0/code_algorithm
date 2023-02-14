function solution(progresses, speeds) {
    const queue=[...progresses].map((i,idx)=>[i,idx])
    let days=1
    
    const result=[]
    while(queue.length){
        const [progress,idx]=queue.shift()
        console.log(progress,idx)
        while(100>progress+speeds[idx]*days){
            console.log('a')
            days++
        }
        result.push(days)
    }
    console.log(result)

    const deployDay=result.reduce((all,i)=>{
        if(i in all){
            all[i]+=1
        }else{
            all[i]=1
        }
        return all
    },{})

    console.log(deployDay)
    
   return Object.values(deployDay)
}