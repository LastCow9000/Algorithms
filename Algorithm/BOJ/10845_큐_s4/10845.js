// boj 10845 큐 s4
// noj.am/10845

class queue {
  constructor() {
    this.arr = [];
  }

  push(num) {
    this.arr.push(num);
  }

  pop() {
    return this.arr.shift() || -1;
  }

  size() {
    return this.arr.length;
  }

  empty() {
    return this.arr.length ? 0 : 1;
  }

  front() {
    return this.arr[0] || -1;
  }

  back() {
    return this.arr[this.arr.length - 1] || -1;
  }
}

const fs = require('fs');
const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : ``
).split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const f = () => {
  const q = new queue();
  let N = parseInt(input());
  let ans = '';

  while (N--) {
    const cmd = input().trim().split(' ');

    if (cmd[0] === 'push') q.push(parseInt(cmd[1]));
    else if (cmd[0] === 'pop') ans += q.pop() + '\n';
    else if (cmd[0] === 'size') ans += q.size() + '\n';
    else if (cmd[0] === 'empty') ans += q.empty() + '\n';
    else if (cmd[0] === 'front') ans += q.front() + '\n';
    else if (cmd[0] === 'back') ans += q.back() + '\n';
  }

  console.log(ans);
}

f();