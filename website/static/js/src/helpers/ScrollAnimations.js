import ScrollObserver from "./ScrollObserver.js"

// Animation classes
const FADE_IN = "willFadeIn"
const FADE_IN_CUSTOM = "willFadeInCustom"
const FADE_IN_FROM_BOTTOM = "willFadeFromBottom"
const FADE_IN_FROM_TOP = "willFadeFromTop"
const FADE_IN_FROM_LEFT = "willFadeFromLeft"
const FADE_IN_FROM_RIGHT = "willFadeFromRight"

// Ratio of visibility at which to reveal elements
const REVEAL_RATIO = 0.2

const ScrollAnimations = {
	init() {
		// Prep all elements with hard-coded animations
		this.prepareHardcodedAnimations(FADE_IN_FROM_BOTTOM, [
			".practice-areas div div",
			".clients .client",
			".leadership .person",
			".work-sample-page .flex-container",
			".work-grid-preview",
		])
		this.prepareHardcodedAnimations(FADE_IN_FROM_LEFT, [
			".origin-and-mission .flex-item",
			".work-sample.default .image",
			".work-sample.default .looping-video",
			".work-sample.reverse .client",
			".work-sample.reverse .title",
		])
		this.prepareHardcodedAnimations(FADE_IN_FROM_RIGHT, [
			".origin-and-mission.reverse .flex-item",
			".work-sample.default .client",
			".work-sample.default .title",
			".work-sample.reverse .image",
			".work-sample.reverse .looping-video",
		])
		this.prepareHardcodedAnimations(FADE_IN_CUSTOM, [
			".discipline__work-sample",
		])

		// Add the scroll observer to all animatable elements and
		// call the reveal function when they intersect with the viewport
		ScrollObserver.init(".anim", this.reveal)
	},

	/**
	 *  Prepares elements that have been hard-coded to animate. Finds elements matching
	 *  the provided selectors and adds the "pre-animation" classes necessary to create
	 *  that effect.
	 */
	prepareHardcodedAnimations(animationClass, selectors) {
		selectors.forEach((selector) => {
			Array.from(document.querySelectorAll(selector)).forEach((element) => {
				element.classList.add("anim")
				if (animationClass) element.classList.add(animationClass)
			})
		})
	},

	/**
	 *  Reveals an element as it's scrolled into view by adding the '.anim-complete' class
	 *  when it's over 20% in view.
	 */
	reveal(event, observer) {
		const { target } = event[0]
		const intersectionRatio = event[0].intersectionRatio
		// if element is far enough in the viewpoint, animate in
		if (intersectionRatio > REVEAL_RATIO) {
			if (!target.classList.contains("anim-complete")) {
				target.classList.add("anim-complete")
			}
		}
	},
}

export default ScrollAnimations
