/*
	Element that triggers an animated scroll to reveal featured work samples
	on click
*/
const ScrollIndicator = {
	
	indicator: null,
	nav: null,
	firstWorkSample: null,

	/*
		Bind elements and init scroll
	*/
	init() {
		this.indicator = document.querySelector("#scroll-indicator")
		this.nav = document.querySelector(".nav")
		this.firstWorkSample = document.querySelector(".work-sample")
		if (!this.nav || !this.indicator || !this.firstWorkSample) { return }

		this.scroll()
	},

	/*
		Animated scroll to first work sample on indicator click
	*/
	scroll() {
		const offset = this.computeOffset()
		this.indicator.addEventListener("click", () => {
			$("html, body").animate({
				scrollTop: $(".work-sample").offset().top - offset
			}, 500)
		})
	},

	/*
		Calculates vertical offset so that the first work sample is 
	*/
	computeOffset() {
		// get all computed styles
		const navStyles = window.getComputedStyle(this.nav)
		const navHeight = parseInt(navStyles.getPropertyValue('height'))
		const workSampleStyles = window.getComputedStyle(this.firstWorkSample)
		const workSampleMarginTop = parseInt(workSampleStyles.getPropertyValue('margin-top'))

		// return offset
		return (navHeight + workSampleMarginTop)
	},
}

export default ScrollIndicator