function quickSort(arr){
  if(arr.length <= 1) return arr

  let index = 0
  let pivot = arr[index];

  for(let i = 1; i < arr.length; i++){
    if (arr[i] < pivot && i > index){
      let [ item ] = arr.splice(i, 1)
      arr.unshift(item)
      index++
    }
    else if (arr[i] > pivot && i < index){
      let [ item ] = arr.splice(i, 1)
      arr.push(item)
      index--
    }
  }
  
  const left = quickSort(arr.slice(0, index))
  const right = quickSort(arr.slice(index + 1))

  
  return [...left, pivot, ...right]
}

console.log(quickSort([5, 3, 7, 4, 6, 2, 8, 1]))
