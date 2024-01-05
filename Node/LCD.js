const {lcd, write}  = require('./LCDConfig')

lcd.on('ready', _ => {
  console.log('LCD ready')
  write('Hello', 1)
  setInterval(_ => {
    lcd.scrollDisplayRight()
  }, 500);
  /*
  setInterval(_ => {
    write('Current Time: ' + new Date().toISOString().substring(11, 19))
  }, 1000);
  */
});

// If ctrl+c is hit, free resources and exit.
process.on('SIGINT', _ => {
  console.log('peace out')
  write('Goodbye')
  lcd.close();
  process.exit();
});
