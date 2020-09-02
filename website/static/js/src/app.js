// NPM imports
import "fetch-polyfill"
import "babel-polyfill"

// Local styles
import styles from "../../css/src/app.scss"



// Initialize components on document ready
$(document).ready(function() {
	// Throttle the resize method
	let resizeId = null
	$(window).resize(() => {
		clearTimeout(resizeId)
		resizeId = setTimeout(initResizeComponents, 500)
	})
})

// Resize initializers
let initResizeComponents = function() {
	console.log('resize')
}
