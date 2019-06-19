/**
 * Sort array using selection sort algorithm
 * @param {Array} arr
 */

function selectionSort(arr){
  let index = 0;
  let sorted = false;

  while (index < arr.length && !sorted){
    let iSmallest = index;
    sorted = true;
    
    // use for loop instead of forEach to avoid
    // looping over already sorted items
    for (let i = index + 1; i < arr.length; i++){
      if (arr[i] <= arr[iSmallest]){
        sorted = false;
        iSmallest = i;
      }
    }

    let [ smallestItem ] = arr.splice(iSmallest, 1);
    arr.splice(index, 0, smallestItem);

    index++;
  }

  return arr;
}


console.log(selectionSort([2, 3, 5, 1, 7, 2, 8, 9]))
