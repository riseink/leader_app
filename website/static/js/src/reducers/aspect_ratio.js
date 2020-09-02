const initialState = { screen: 'LANDSCAPE' }

const aspect_ratio = (state = initialState, action) => {
	switch(action.type) {
	case 'NEW_ASPECT_RATIO':
		return {...state, screen: action.payload }
	default:
		return state
	}
}

export default aspect_ratio