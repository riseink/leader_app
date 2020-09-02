import store from '../store';

var IntroVideos = {
	video: null,
	currentIndex: 0,

	init() {
		const wrapper = document.getElementById("intro_videos")
		if (!wrapper) { return } // early return if no intro videos

		this.initStateListener();
		this.getVideoData();
		this.bindVideo();
		this.render(store.getState().intro_videos);
	},

	/*
		Subscribe to the store and render with the
		intro_videos state
	*/
	initStateListener() {
		store.subscribe(() =>
			this.render(store.getState().intro_videos)
		)
	},

	/*
		Fetch the video json objects and
		add them to the store if store is empty
	*/
	getVideoData() {
		if(!store.getState().intro_videos.videos) {
			$.get('/api/v2/pages/?format=json&type=website.HomePage&fields=intro_videos', (result) => {
				store.dispatch({ type: "LOADED_VIDEOS", videos: result.items[0].intro_videos })
			})
		}
	},

	bindVideo() {
		let wrapper = document.getElementById("intro_videos")
		this.video = wrapper.getElementsByTagName('video')[0]
	},

	/*
		Changes videos when the current video ends
	*/
	initVideoSwapper() {
		this.video.loop = false
		this.video.onended = () => {
			this.changeVideo()
		}
	},

	/*
		Gets the next video and replaces the current source with 
		the next video's source
	*/
	changeVideo() {
		let next_source = this.getSource(this.shuffleVideos())
		let source = this.getSource(this.video)

		// keep getting new "next source"'s until its different from the current source
		while(source == next_source) {
			next_source = this.getSource(this.shuffleVideos())
		}

		// clone the video node and pass it the next source
		this.cloneVideo(next_source)
	},

	cloneVideo(next_src) {
		// make a copy of the current video node and update src
		let video_copy = this.video.cloneNode(true)
		video_copy.getElementsByTagName('source')[0].src = next_src

		// append the newly created video node to the video container
		this.video.parentElement.appendChild(video_copy)
		this.video = video_copy
		this.video.load()

		this.video.onplay = () => this.removeOldVideo()
		this.video.onended = () => this.changeVideo()
	},

	/*
		Returns the <video> element from a video HTML block
	*/
	removeOldVideo() {
		let wrapper = document.getElementById("intro_videos")
		let old_video = wrapper.getElementsByTagName('video')[0]
		if(wrapper.getElementsByTagName('video').length > 1) {
			old_video.remove();	
		}
	},

	/*
		Sets currentIndex to a randomly selected number, and gets the 
		video at that index
	*/
	shuffleVideos() {
		let state = store.getState().intro_videos
		this.currentIndex = this.selectRandomIndex()
		let parsed = this.parseHTMLString(this.getVideoBlock())
		return parsed.getElementsByTagName('video')[0]		
	},

	/*
		Returns a random number between 0 and the # of videos in the store
	*/
	selectRandomIndex() {
		let state = store.getState().intro_videos
		return Math.floor(Math.random()*state.videos.length)
	},

	/*
		Returns the first <source> element from a video HTML block
	*/	
	getSource(vid) {
		return vid.getElementsByTagName('source')[0].src
	},

	/*
		Returns the first <video> element from a video HTML block
	*/
	getVideoEl(block) {
		return block.getElementsByTagName('video')[0]
	},

	/*
		Parses an HTML string
	*/
	parseHTMLString(html_string) {
		let parser = new DOMParser()
		return parser.parseFromString(html_string, "text/html")
	},

	/*
		Swaps videos by settings a new src attribute 
		on the video's <source> element.
	*/
	swapSource(new_video) {
		const new_src = this.getSource(new_video)
		this.video.getElementsByTagName('source')[0].src = new_src
		
		// play the video
		this.video.load()
	},

	/*
		Gets a new video block based on current screen aspect ratio.
	*/
	getVideoBlock() {
		
		let videoWrapper = document.getElementById("intro_videos")
		let screen_state = store.getState().aspect_ratio
		if(!screen_state) { return }
		let video_state = store.getState().intro_videos

		switch(screen_state.screen) {
			case 'LANDSCAPE':
				videoWrapper.classList.remove('contain')
				videoWrapper.classList.add('cover')
				return video_state.videos[this.currentIndex].video_block_landscape
			case 'PORTRAIT':
				videoWrapper.classList.remove('cover')
				videoWrapper.classList.add('contain')
				return video_state.videos[this.currentIndex].video_block_portrait
			case 'CLASSIC':
				videoWrapper.classList.remove('cover')
				videoWrapper.classList.add('contain')
				return video_state.videos[this.currentIndex].video_block
		}
	},
	
	

	/*
		Renders the first video 
	*/
	renderFirstVideo() {
		// get the next video block HTML
		const block = this.getVideoBlock()

		// extract the video element
		const parsed = this.parseHTMLString(block)
		const next_video = parsed.getElementsByTagName('video')[0]

		// swap out the old source for the next video's source
		this.swapSource(next_video)

		// remove loader
		this.removeLoader()
		
	},

	removeLoader() {

		// show video
		document.querySelector('#intro_videos').classList.remove('intro-videos-hidden')
		
		// remove loader
		const loader = document.querySelector('#home-loader')
		if (!loader) { return }
			
		loader.parentNode.removeChild(loader)

	},

	render(state) {
		if(state.videos) {
			this.currentIndex = this.selectRandomIndex()
			if (state.videos.length > 1) { this.initVideoSwapper() }
			this.renderFirstVideo()
		}
	}
}

export default IntroVideos;
