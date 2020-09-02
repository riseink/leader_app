import store from '../store';

const LANDSCAPE = 16/9
const CLASSIC = 7/8
const PORTRAIT = 70/100

let getDimensions = function() {
	let width = window.innerWidth;
	let height = window.innerHeight;

	return { w: width, h: height }
}

let getAspectRatio = function() {
	let dimensions = getDimensions()

	return dimensions.w / dimensions.h
}

let dispatchIfChanged = function(name) {
	let current_screen = store.getState().aspect_ratio.screen

	if (current_screen != name) {
		store.dispatch({ type: "NEW_ASPECT_RATIO", payload: name })	
	}
}


const AspectRatio = {
	init() {

		let ratio = getAspectRatio()

		if(ratio > CLASSIC) {
			dispatchIfChanged("LANDSCAPE")
		} else if(ratio < CLASSIC && ratio > PORTRAIT) {
			dispatchIfChanged("CLASSIC")
		} else {
			dispatchIfChanged("PORTRAIT")
		}
	}


}

export default AspectRatio;