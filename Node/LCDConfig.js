/**
 * `node LCD` to run
 * https://www.npmjs.com/package/lcd
 */


const LCD = require('lcd') // import LCD from 'lcd'

// Define GPIO to LCD mapping
const LCD_RS = 26 // 7
const LCD_E  = 19 // 8
const LCD_D4 = 13 // 25
const LCD_D5 =  6 // 24
const LCD_D6 =  5 // 23
const LCD_D7 = 11 // 18

const lcd = new LCD({
  rs: LCD_RS,
  e: LCD_E,
  data: [LCD_D4, LCD_D5, LCD_D6, LCD_D7],
  cols: 16,
  rows: 2,
})

const write = (data, row=0, col=0) => {
  lcd.setCursor(col, row)
  lcd.print(data, (err) => {
      if(err) {
        throw err;
      }
  })
}

module.exports = {
  lcd,
  write,
}
