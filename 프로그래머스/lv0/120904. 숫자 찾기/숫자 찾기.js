
const solution = (num,k) => {
 return [...num+''].indexOf(k+'') !== -1 ? [...num+''].indexOf(k+'')+1 : -1
}

