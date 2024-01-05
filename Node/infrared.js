// https://www.npmjs.com/package/mlx90614
const {celToFah} = require('./helpers')
const MLX906614 = require('mlx90614')
const execSync = require('child_process').execSync
const exec = (cmd) => execSync(cmd, {encoding: 'utf-8' }) 
const getCurrentI2C = () => parseInt(exec('sudo raspi-config nonint get_i2c'), 10)

const ENABLED = 0
const DISABLED = 1

const initialI2C = getCurrentI2C()
console.log(`initial i2c: ${initialI2C === DISABLED ? 'disabled' : 'enabled'} (${initialI2C})`)

const toggleI2C = (state) => {
  console.log(`${state === DISABLED ? 'disabling' : 'enabling'} i2c`)
  exec(`sudo raspi-config nonint do_i2c ${state}`);
  const current = getCurrentI2C()
  console.log(`i2c: ${current === DISABLED? 'disabled' : 'enabled'}`)
}

const sensor = new MLX906614()
const getTemp = () => {
  sensor.readObject((_, cel) => {
    const fah = Math.floor(celToFah(cel))
    cel = Math.floor(cel)
    console.log(`Current temp: \n\t${cel}c (${fah}f)`)
  })
}


if (initialI2C === DISABLED) {
  toggleI2C(ENABLED)
}

const tempInterval = setInterval(getTemp, 1000)

setTimeout(() => {

  clearInterval(tempInterval)

  //@TODO disable i2c on exit
  if (initialI2C === DISABLED) {
    toggleI2C(DISABLED)
  }
}, 20000)



