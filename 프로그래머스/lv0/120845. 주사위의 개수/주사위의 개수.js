function solution(box, n) {
 const [width, Depth, height] = box;
    const result = Math.floor(width/n) * Math.floor(Depth/n) * Math.floor(height / n);
    
    return result;
}

