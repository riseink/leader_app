var LazyLoad = {
	observer: null,

	init() {
		this.getMediaElements().then((result) => {
			this.initObserver()
			this.attachObserver(result)
		}, (err) => {
			if (process.env.NODE_ENV === "development") {
				console.log(err)
			}
		})
	},

	initObserver() {
		this.observer = new IntersectionObserver((entries, observer) => {
			entries.forEach((entry) => {
				if(entry.isIntersecting) {
					let media = entry.target
					this.handleIntersect(media)	
					this.destroyObserver(media)
				}
			})
		})
	},

	getMediaElements() {
		return new Promise((resolve, reject) => {
			// Get the elements with a .lazy class
			let results = [].slice.call(document.querySelectorAll(".lazy"))
			
			// Resolve the promise if elements are found
			if (results.length > 0) {
				resolve(results)	
			} else {
				reject("No items to lazy load")
			}
		})
	},

	attachObserver(elements) {
		elements.forEach((el) => {
			this.observer.observe(el)
		})
	},

	handleIntersect(el) {
		switch(el.tagName) {
			case 'VIDEO':
				this.lazyLoadVideo(el)
				break;
			case 'IMG':
				this.swapSource(el)
				break;
		}		
	},

	lazyLoadVideo(el) {
		let sourceTags = el.getElementsByTagName('source')

		for(let i = 0; i < sourceTags.length; i++) {
			this.swapSource(sourceTags[i]);
			el.load();
		}

	},

	swapSource(el) {
		el.src = el.dataset.src
	},

	destroyObserver(el) {
		el.classList.remove("lazy")
		this.observer.unobserve(el)
	}	
}

export default LazyLoad