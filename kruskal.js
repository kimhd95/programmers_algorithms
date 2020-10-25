function createUnionFind(n) {
    const arr = []
    for(let i=0; i<n; i++) {
        arr.push(i)
    }
    return arr
}

function getParent(parents, i) {
  if (parents[i] === i) return [parents, i]
  else {
    [parents, parents[i]] = getParent(parents, parents[i])
    return [parents, parents[i]]
  }
}

// 합칠 때는 더 작은 값으로 합침
function unionParent(parents, n1, n2) {
  const p1 = getParent(parents, n1)[1]
  const p2 = getParent(parents, n2)[1]
  if (p1 < p2) parents[p2] = p1
  else parents[p1] = p2
  return parents
}

function findParent(parents, n1, n2) {
  const p1 = getParent(parents, n1)[1]
  const p2 = getParent(parents, n2)[1]
  if (p1 === p2) return true
  else return false
}

function isCycle(parents, n1, n2) {
  return findParent(parents, n1, n2)
}


/////////////////////////////

function solution(n, edges) {
  let cost = 0
  let parents = createUnionFindTable(n)
  edges.sort((a, b) => a[2] - b[2])
  // console.log(edges)
  for (let i = 0; i < edges.length; i++) {
    const [n1, n2, c] = edges[i]
    if (isCycle(parents, n1, n2)) {
      continue
    }
    parents = unionParent(parents, n1, n2)
    cost += c
  }
  return cost
}
