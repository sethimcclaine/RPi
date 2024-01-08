/**
 * This was create to compare the IR Temp sensor (mlx9066614)
 * to the probe sensor (ds18b20) to demonstrate, through the LCD
 * screen, the IR sensor is not tracking correctly.
 **/
const { lcd,write } = require('./LCDConfig')
const { celToFah } = require('./helpers')
const MLX906614 = require('mlx90614')
const DS18B20 = require('ds18b20')

let probeSensor
const irSensor = new MLX906614()
let pCel, pFah, iCel, iFah = 0
const tempFormat = (n) => {
  const floor = Math.floor(n*10).toString()
  return floor.slice(0,2)+'.'+floor.slice(2)
}

const getIRTemp = () => 
  irSensor.readObject((_, c) => {
    iCel = c
    iFah = celToFah(c)
  })
const getProbeTemp = () => {
  pCel = DS18B20.temperatureSync(probeSensor)
  pFah = celToFah(pCel)
}

let tempInterval;
const init = async () => {
  await DS18B20.sensors((err, ids) => {
    ids.filter((id) => !id.indexOf('28-'))
    probeSensor=ids[0]
    console.log(`Probe Id: ${probeSensor}`)
  });
  lcd.on('ready', () => {
    console.log('LCD ready')
    write(`Probe :: iRed`, 0)
    tempInterval = setInterval(() => {
      getProbeTemp()
      getIRTemp()
      write(`${tempFormat(pCel)}c :: ${tempFormat(iCel) || '00.0'}c`, 1)
    }, 1000)
  })
  process.on('SIGNINT', () => {
    console.log('peace out')
    clearInterval(tempInterval)
  }, 20000)
}


init()
