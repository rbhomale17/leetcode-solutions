/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise((Resolve)=>{
        return setTimeout(Resolve, millis)
    })
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */

