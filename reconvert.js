const fs = require('fs')
const path = require('path')

if (!fs.existsSync('paratranz'))
  fs.mkdirSync('paratranz')
if (!fs.existsSync('game/tl/chinese'))
  fs.mkdirSync('game/tl/chinese', { recursive: true })

const escape = (str) => {
  if (!str) return str
  return str.replace(/(?<!\\)"/g, '\\"')
}

const reconvert = () => {
  const files = fs.readdirSync('game/tl/chinese').filter(file => /\.rpy$/.test(file))
  for (const file of files) {
    const basename = path.basename(file, '.rpy')
    // let result = `# TODO: Translation updated at ${new Date().toLocaleString()}\n`
    const [head] = fs.readFileSync(`game/tl/chinese/${file}`, 'utf-8').split('\n')
    let result = head + '\n'
    if (fs.existsSync(`paratranz/${basename}.json`)) {
      const dialogues = JSON.parse(fs.readFileSync(`paratranz/${basename}.json`, 'utf-8'))
      for (const { key, context, original, translation } of dialogues) {
        const [, source, line] = context.match(/blob\/[^\/]+\/(.+)#L(\d+)/)
        let [, speaker] = context.match(/^说话人: ([^\n]+)/)
        if (speaker.includes('无')) {
          speaker = ''
        }

        result += `
# ${decodeURI(source)}:${line}
translate chinese ${key}:

    # ${speaker}"${original}"
    ${speaker}"${escape(translation) ?? ''}"\n`
      }
    }
    if (fs.existsSync(`paratranz/${basename}_strings.json`)) {
      const strings = JSON.parse(fs.readFileSync(`paratranz/${basename}_strings.json`, 'utf-8'))
      result += '\ntranslate chinese strings:\n'
      for (const { context, original, translation } of strings) {
        const [, source, line] = context.match(/blob\/[^\/]+\/(.+)#L(\d+)/)
        result += `
    # ${decodeURI(source)}:${line}
    old "${original}"
    new "${escape(translation) ?? ''}"\n`
      }
    }
    fs.writeFileSync(`game/tl/chinese/${file}`, result + '\n')
  }
}

try {
  reconvert()
} catch (error) {
  console.error(error)
}