const fs = require('fs')
const path = require('path')
const crypto = require('crypto')

function md5sum(filePath) {
    const hash = crypto.createHash('md5')
    const data = fs.readFileSync(filePath)
    hash.update(data, 'utf8')
    return hash.digest('hex')
}
const allBIOS = []
const filePath = path.join(__dirname, 'System.dat')
const md5 = md5sum(filePath)

const data = fs.readFileSync(filePath).toString()
const lines = data.split('\n')
lines.forEach(line => {
    const match = line.match(/rom \( name (.+) size (\d+) crc (.+) md5 (.+) sha1 (.+) \)/)
    if (match) allBIOS.push({ filename: match[1].replace(/\"/g, ''), md5: match[4] })
})

describe('all files md5sum check', () => {
    test(`md5sum("System.dat") should be "f608bbe045dcfa5b8e4f4bbb9ed8070d"`, () => {
        expect(md5).toEqual('f608bbe045dcfa5b8e4f4bbb9ed8070d')
    })
    allBIOS.forEach(bios => {
        const { filename, md5 } = bios
        test(`md5sum("${filename}") should be "${md5}"`, () => {
            const filepath = path.join(__dirname, '..', 'BIOS', filename)
            expect(md5sum(filepath)).toEqual(md5)
        })
    })
})
