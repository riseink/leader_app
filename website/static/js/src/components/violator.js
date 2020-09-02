import store from '../store'

const SHOW_VIOLATOR_DELAY = 100

const Violator = {

	violator: null,
	violatorBtn: null,

	init() {
		
		this.violator = document.querySelector('.violator')
		this.violatorBtn = document.querySelector('#violator-close')

		// if there is a violator on this page (hidden or not)
		if (this.violator && this.violatorBtn) {

			// listen for changes
			this.initClickListener()
			this.initStateListener()

			// if violator has not previously been hidden during this session, display it
			if (window.sessionStorage.getItem('violatorVisible') !== 'false') {
				this.showViolator()
			} else {
				store.dispatch({type: 'TOGGLE_VIOLATOR'})
			}

		} else {
			store.dispatch({type: 'TOGGLE_VIOLATOR'})
		}
	},

	// toggle violator on icon clicks
	initClickListener() {
		this.violatorBtn.addEventListener('click', event => {
			event.preventDefault()
			store.dispatch({type: 'TOGGLE_VIOLATOR'})
		})
	},

	// listen for store changes and re-render on each
	initStateListener() {
		store.subscribe(() => this.render(store.getState().violator))
	},

	updateSessionStorage(violatorVisible) {
		window.sessionStorage.setItem('violatorVisible', violatorVisible);
	},

	showViolator() {
		// display violator after <SHOW_VIOLATOR_DELAY> milliseconds
		setTimeout(() => {
			this.violator.style.transform = 'translateY(0%)';
		}, SHOW_VIOLATOR_DELAY)
	},

	// render the violator with or without 'hidden' class
	render(state) {
		this.updateSessionStorage(state.violatorVisible);
		(state.violatorVisible) ? this.violator.classList.remove('hidden') : this.violator.classList.add('hidden')
	}

}

export default Violator