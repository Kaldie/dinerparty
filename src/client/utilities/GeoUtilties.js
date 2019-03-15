
import 'promise'

let cachedLocation=null

setInterval(() => {
  cachedLocation=null
}, 60000);

export default function() {
  return new Promise(function(resolve, reject) {
    if (cachedLocation) {
      resolve(cachedLocation)
    }
    else if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        cachedLocation = position
        resolve(position)
      }, reject);
    } else {
      reject("Navigation.geolocation is not available")
    }
  })
}
