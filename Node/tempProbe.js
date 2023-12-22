const ds18b20 = require('ds18b20');
/**
 * sensorId
 * `ls /sys/bus/w1/devices` 
 * starts with '28-xxxxxxxx'
 */

const init = async () => {
  let sensors = []
  await ds18b20.sensors((err, ids) => {
    // get sensor IDs ...
    console.log('Sensors:', ids)
    ids.filter((id) => !id.indexOf('28-'))
    console.log('Cleaned Sensors', ids)
    sensors = ids
  });

console.log('sensors recieved', sensors)
  setInterval(() => {
    sensors.forEach((sensorId) => {
      const cel = ds18b20.temperatureSync(sensorId)
      const f = cel * 9 / 5 + 32
      console.log(`Current temp for ${sensorId} is ${cel}c (${f}f)`)
    })
  }, 1000)

/*
  // ... async call
  ds18b20.temperature(sensorId, (err, value) => {
    console.log('Current temperature is', value);
  });

  // ... or sync call
  console.log('Current temperature is' + ds18b20.temperatureSync(sensorId));

  // default parser is the decimal one. You can use the hex one by setting an option
  ds18b20.temperature(sensorId, {parser: 'hex'}, function(err, value) {
    console.log('Current temperature is', value);
  });

  console.log('Current temperature is' + ds18b20.temperatureSync(sensorId, {parser: 'hex'}));
*/
}
init();
