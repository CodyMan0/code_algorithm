const solution = (my_string) => {

    
    
let array = my_string.split('')
let result =[];
         
for (let i = 0; i < array.length; i ++ ) {
    if(array[i] === array[i].toLowerCase()) {
        result.push(array[i].toUpperCase());
    }
    
    if(array[i] === array[i].toUpperCase()) {
        result.push(array[i].toLowerCase());
    }
}
    
     return result.join('')
                 }
                                       