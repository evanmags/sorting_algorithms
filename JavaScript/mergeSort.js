function mergeSort(arr){
  let right, left;

  if(arr.length <= 1){
    return arr;
  }
  else{
    let breakPoint = Math.floor(arr.length / 2);
    right = mergeSort(arr.slice(breakPoint));
    left = mergeSort(arr.slice(0, breakPoint));
  }

  const sortedArr = [];
  let ri = 0 
  let li = 0 

  while (right.length > ri && left.length > li) {
    if(right[ri] < left[li]){
      sortedArr.push(right[ri])
      ri++
    }
    else{
      sortedArr.push(left[li])
      li++
    }
  }
  
  while (ri != right.length){
    sortedArr.push(right[ri])
    ri++
  }
  while (li != left.length){
    sortedArr.push(left[li])
    li++
  }

  return sortedArr;
}

console.log(mergeSort([5, 3, 7, 4, 6, 2, 8, 1]))
