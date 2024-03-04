A1 = [1, 2, 4, 5, 6, 6, 8, 9];
A2 = [2, 5, 6, 7, 8, 8, 9];

function findClosestNum(arr, targetNum) {
  let minDiff = minDiffLeft = minDiffRight = Number.MAX_SAFE_INTEGER
  let low = 0, high = arr.length-1, closestNum = null; 

  if (arr.length ===0) return closestNum;
  if(arr.length === 1) return arr[0];

  while( low <= high){
    let mid = Math.floor((low+high)/2)

    if (mid+1 < arr.length) {
      minDiffRight = Math.abs(arr[mid+1] - targetNum)
    }

    if(mid >  0){
      minDiffLeft = Math.abs(arr[mid - 1] - targetNum);
    }


    if(minDiffLeft < minDiff){
      minDiff = minDiffLeft
      closestNum = A[mid-1]
    }
    if(minDiffRight < minDiff){
      minDiff = minDiffRight
      closestNum = A[mid+1]
    }


  }
  return closestNum
}
// protip: return value first thing writing Js