const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

function md5sum(filePath) {
    const hash = crypto.createHash("md5");
    const data = fs.readFileSync(filePath);
    hash.update(data, "utf8");
    return hash.digest("hex");
}
const allBIOS = [];
const filePath1 = path.join(__dirname, "System.dat");
const data1 = fs.readFileSync(filePath1).toString();
const lines1 = data1.split("\n");
lines1.forEach((line) => {
    const match = line.match(
        /rom \( name (.+) size (\d+) crc (.+) md5 (.+) sha1 (.+) \)/
    );
    if (match)
        allBIOS.push({ filename: match[1].replace(/\"/g, ""), md5: match[4] });
});
const filePath2 = path.join(__dirname, "MoreBIOS.dat");
const data2 = fs.readFileSync(filePath2).toString();
const lines2 = data2.split("\n");
lines2.forEach((line) => {
    const match = line.match(
        /rom \( name (.+) size (\d+) crc (.+) md5 (.+) sha1 (.+) \)/
    );
    if (match)
        allBIOS.push({ filename: match[1].replace(/\"/g, ""), md5: match[4] });
});

describe("all files md5sum check", () => {
    allBIOS.forEach((bios) => {
        const { filename, md5 } = bios;
        test(`md5sum("${filename}") should be "${md5}"`, () => {
            const filepath = path.join(__dirname, "BIOS", filename);
            expect(md5sum(filepath)).toEqual(md5);
        });
    });
});
