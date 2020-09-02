const initialState = { videos: null }

const intro_videos = (state = initialState, action) => {
	switch(action.type) {
	case 'LOADED_VIDEOS':
		return {...state, videos: action.videos }
	default:
		return state
	}
}

export default intro_videos