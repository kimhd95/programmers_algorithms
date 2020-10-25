class Node {
  constructor(data) {
    this.data = data;
    this.children = [];
  }

  add(data) {
    this.children.push(new Node(data))
  }

  remove() {
    return this.children.pop()
  }
}

class Tree {
  constructor(rootNode=null) {
    this.root = rootNode
  }

  bfs(fn) {
    if (this.root === null) return;

    const unvisitedQueue = [this.root]
    while (unvisitedQueue.length > 0) {
      const cur = unvisitedQueue.shift()
      unvisitedQueue.push(...cur.children)
      fn(cur)
    }
  }

  dfs(fn) {
    if (this.root === null) return;

    const unvisitedStack = [this.root]
    while (unvisitedStack.length > 0) {
      const cur = unvisitedStack.pop()
      unvisitedStack.push(...cur.children)
      fn(cur)
    }
  }
}

// const t = new Tree(new Node('123'))
// console.log(t)
