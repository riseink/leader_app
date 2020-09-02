import store from "../store"

var Menu = {
	el: null,

	init() {
		this.el = document.getElementById("nav_menu")
		this.initStateListener()
		this.render(store.getState().navigation)
	},

	initStateListener() {
		store.subscribe(() => this.render(store.getState().navigation))
	},

	render(state) {
		if (state.menuVisible) {
			this.el.classList.add("open")
			// delay so that showing/hiding of scrollbar takes place during menu slide in
			setTimeout(() => {
				document
					.querySelector("body")
					.classList.add("disallow-scroll")
			}, 150)
		} else {
			this.el.classList.remove("open")
			// delay so that showing/hiding of scrollbar takes place during menu slide in
			setTimeout(() => {
				document
					.querySelector("body")
					.classList.remove("disallow-scroll")
			}, 150)
		}
	}
}

export default Menu