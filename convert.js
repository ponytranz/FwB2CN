const fs = require('fs')
const path = require('path')

if (!fs.existsSync('paratranz'))
  fs.mkdirSync('paratranz')
if (!fs.existsSync('game/tl/chinese'))
  fs.mkdirSync('game/tl/chinese', { recursive: true })

const buildUrl = (file) => {
  const path = encodeURI(file)
  const url = /^renpy\/common/.test(file)
    ? 'https://github.com/renpy/renpy/blob/master/' + path
    : 'https://github.com/ponytranz/FwB2CN/blob/empty/' + path
  return url
}

const convert = () => {
  const files = fs.readdirSync('game/tl/chinese').filter(file => /\.rpy$/.test(file))
  for (const file of files) {
    const dialogues = []
    const basename = path.basename(file, '.rpy')
    const content = fs.readFileSync(`game/tl/chinese/${file}`, 'utf-8')
    for (const match of content.matchAll(
      /# (game\/.+\.rpym?):(\d+)\s+translate chinese (.+):\s+# (.+ )?"(.+)"\s+(.+ )?"(.+)?"/g
    )) {
      /*
      match[1] : file
      match[2] : line number
      match[3] : text key
      match[4] : speaker original
      match[5] : text original
      match[6] : speaker translated
      match[7] : text translated
      */
      dialogues.push({
        key: match[3],
        original: match[5],
        context: `说话人: ${match[4] ?? '无 '}\n代码: ${buildUrl(match[1])}#L${match[2]}`
      })
    }
    if (dialogues.length) {
      fs.writeFileSync(
        `paratranz/${basename}.json`,
        JSON.stringify(dialogues, null, 2))
    }
    const strings = []
    let current = '', cnt
    for (let match of content.matchAll(
      /# ((.+):(\d+))\s+old "(.+)"\s+new "(.+)?"/g
    )) {
      /*
      match[1] : file and line number
      match[2] : file
      match[3] : line number
      match[4] : text original
      match[5] : text translated
      */
      if (match[1] !== current) {
        // 多个文件可能对应同一个文件行号
        current = match[1]
        cnt = 0
      }
      const key = `${match[2]}_L${match[3]}_${cnt}`
      cnt += 1
      strings.push({
        key,
        original: match[4],
        context: `代码: ${buildUrl(match[2])}#L${match[3]}`
      })
    }
    if (strings.length) {
      fs.writeFileSync(
        `paratranz/${basename}_strings.json`,
        JSON.stringify(strings, null, 2))
    }
  }
}

try {
  convert()
} catch (error) {
  console.log(error)
}
