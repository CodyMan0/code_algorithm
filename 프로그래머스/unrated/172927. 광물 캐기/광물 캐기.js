
function solution(picks, minerals) {
    const converted = minerals.map(el=>{
        if(el === "diamond") return 0;
        if(el === "iron") return 1;
        if(el === "stone") return 2;
    });

    const result = [];

    const countF = (picks, arr, count) => {
        if(picks.every(el=>el === 0)) return result.push(count)

        for(let i = 0; i<picks.length; i++){
            if(picks[i]){
                const tempPick = picks.slice();
                const tempMinerals = arr.slice();
                let tempCount = count;

                let c = 5;
                while(c > 0 && tempMinerals.length){
                    const target = tempMinerals.shift();
                    if(i === 1 && target === 0) {
                        tempCount += 5;
                    } else if (i === 2 && target === 0){
                        tempCount += 25;
                    } else if (i === 2 && target === 1){
                        tempCount += 5;
                    } else {
                        tempCount += 1;
                    };
                    c -= 1;
                };
                if(tempMinerals.length === 0) return result.push(tempCount)
                tempPick[i] -= 1;

                countF(tempPick, tempMinerals, tempCount);
            };
        };
    };
    countF(picks, converted, 0);
    return Math.min(...result);
};




