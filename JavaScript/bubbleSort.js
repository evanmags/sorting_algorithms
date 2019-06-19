function bubbleSort(arr){
  let sortCount = 0;
  let sorted = false;

  while(sortCount < arr.length && !sorted){
    let iLargest = 0;
    sorted = true;

    for(i = 1; i < (arr.length - sortCount); i++){
      if (arr[i] < arr[iLargest]){
        sorted = false;
        let [ item ] = arr.splice(i, 1);
        arr.splice(iLargest, 0, item);
      }

      iLargest = i;
    }

    sortCount++;
  }

  return arr;
}
