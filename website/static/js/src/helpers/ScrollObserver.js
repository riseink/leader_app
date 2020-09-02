/**
 *  
 *  Wrapper object for IntersectionObserver.
 *  
 *  This object is initialized in '/.ScrollAnimations.js', where it's passed 
 *  a selector (what to observe) and a callback function (what to do with the observed element).
 *  
 */


const ScrollObserver = {

    /**
     *  Builds a list of thresholds, which define how frequently 
     *  the callback function is called.
     *  
     *  (more thresholds == more frequently called)
     */
    buildThresholdList(startPoint, numSteps) {
        const thresholds = [];

        for (let i = startPoint; i <= numSteps; i++) {
            const ratio = i / numSteps
            thresholds.push(ratio)
        }

        thresholds.push(0)
        return thresholds
    },

    /**
     *  Creates an IntersectionObserver for each element with the specified selector.
     */
    init(selector, callback) {

        const observables = Array.from(document.querySelectorAll(selector))
        
        const options = {
            root: null,
            rootMargin: '0px',
            threshold: []
        }
        
        observables.forEach(observable => {
            options.threshold = this.buildThresholdList(1.0, 50.0)
            let obs = new IntersectionObserver(callback, options)
            obs.observe(observable)
        })
    }
}

export default ScrollObserver;